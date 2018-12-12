#!/usr/bin/env python
#
#  Create_options.py :
#  Author   Manuel Barbera Asin, 14 November 2005
#  Modified Gloria Corti, 20 Nov 2008 to add SUSY and J/Psi particle guns
#  Modified Patrick Robbe, 15 Sep 2011 for new conventions
#  Modified Marc-Olivier Bettler, to add K_L0 decays support with 38XXXXXX
#
#  create an options file from a decay files
#
#  Event type is GSDCNTXU
#
#============================================================================
# 060616 - fixes
#============================================================================

version = 'v4r1'

bkk_first = True
eventid_inbkk = []
sql_first = True
eventid_insql = []
list_of_obsoletes = []
exit_status = 0
list_of_wg = [ 'QCD' , 'EW' , 'Exotica' , 'Onia' , 'Charm' , 'RD' , 'B2Ch' ,
               'B2OC' , 'BnoC' , 'B2SL' , 'EW' , 'Calo' , 'PID' , 'Tagging' ,
               'Alignement' , 'Lumi', 'Sim' ]

# particle gun momenta files, map of pdg ID : (binning variable, histogram path)

pGunMomentumFileIDs = {413 : ("pteta", "h_pteta"), 
                       445 : ("ptpz", "OutputMomentumSpectrum_ptpz"),
                       10441 : ("ptpz", "OutputMomentumSpectrum_ptpz"),
                       20443 : ("ptpz", "OutputMomentumSpectrum_ptpz"),
                       521 : ("pteta", "h_pteta"),
                       531 : ("pteta", "h_pteta")
                      }

import os , re , string, logging , sys
import time , glob 
from optparse import OptionParser, OptionValueError

class GenericOptionFile(object):
    """ Class to write in an option file
    """
    def __init__( self ):
        self.filename = None
        self.f = None
    def __del__( self ):
        self.Close()
    def Close( self ):
        if self.f:
            self.f.close()
    def OptionFileName( self ):
        return self.filename
    def SetFileName( self , filename ):
        self.filename = os.path.normpath( filename + self.suffix )
    def Open( self ):
        if self.filename:
            self.f = open( self.filename , 'w' )
    def Write( self , lines ):
        """ write the lines in the file
        """
        self.f.writelines( [ l+'\n' for l in lines ] )
    def WriteHeader( self , eventtype , descriptor ):
        lines = [ "{0} file {1} generated: {2}".format( self.comment ,
                                                        self.filename ,
                                                        time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())) ,
                 "{0}".format( self.comment ) ,
                 "{0} Event Type: {1}".format( self.comment , eventtype ) ,
                 "{0}".format( self.comment ) ,
                 "{0} ASCII decay Descriptor: {1}".format( self.comment , descriptor ) ,
                 "{0}".format( self.comment ) ]
        self.Write( lines )
    def AddExtraOptions( self , eventtype ):
        self.AddInclude( eventtype.ExtraOptions() )
    def AddEventTypeNumber( self , eventtype ):
        self.AddOptionValue( 'Generation.EventType' , eventtype.EventTypeNumber() )
    def AddSampleTool( self , eventtype ):
        self.AddOptionValue( 'Generation.SampleGenerationTool' , '"{0}"'.format( eventtype.Sample().split('.')[0] ) )
    def AddEvtGenUserDecayFile( self , eventtype ):
        self.AddOptionValue( 'ToolSvc.EvtGenDecay.UserDecayFile' , '"$DECFILESROOT/dkfiles/{0}.dec"'.format( eventtype.DecayName() ) )
    def AddProductionTool( self , eventtype ):
        self.AddOptionValue( 'Generation.{0}.ProductionTool'.format( eventtype.Sample() ) ,
                            '"{0}Production"'.format( eventtype.Production() ) )
    def AddGenXiccProductionToolBaryonState( self , eventtype ):
        self.AddOptionValue( 'Generation.{0}.{1}Production.BaryonState'.format( eventtype.Sample(), eventtype.Production() ) ,
                             '"{0}"'.format( eventtype.DecayDescriptor().split('->')[0][1:].strip() ) )
    def AddGenXiccBeamMomentum( self , eventtype ):
        self.ConfigureToolAndAlgo( 'Gauss' )
        self.AddOptionValue( 'Generation.{0}.{1}Production.BeamMomentum'.format( eventtype.Sample(), eventtype.Production() ) ,
                             'Gauss().BeamMomentum' )
    def AddCutTool( self , eventtype , CutsValue ):
        self.AddOptionValue( 'Generation.{0}.CutTool'.format( eventtype.Sample() ) ,
                            '"{0}"'.format( CutsValue ) )
    def AddGenXiccCutToolBaryonState( self , eventtype , CutsValue ):
        self.AddOptionValue( 'Generation.{0}.{1}.BaryonState'.format( eventtype.Sample(), CutsValue ) ,
                             'Generation().{0}.{1}Production.BaryonState'.format( eventtype.Sample(), eventtype.Production() ) )
    def GeneratePolarizedLambdab( self ):
        self.AddOptionValue( 'ToolSvc.EvtGenDecay.PolarizedLambdad' , self.true_string )
    def AddParticleValue( self , eventtype ):
        self.AddOptionValue( 'LHCb__ParticlePropertySvc.Particles' ,
                            '{0} {1} {2}'.format( self.list_begin , eventtype.ParticleValue() , self.list_end ) )
    def AddParticleTable( self , eventtype ):
        self.AddOptionValue( 'LHCb__ParticlePropertySvc.OtherFiles' ,
                            '{0}"$DECFILESROOT/ppfiles/{1}.tbl"{2}'.format( self.list_begin , eventtype.ParticleTable() , self.list_end ) )
    def AddSignalPID( self , eventtype , pid ):
        self.AddOptionValue( 'Generation.{0}.{1}.SignalPID'.format( eventtype.Sample() , eventtype.Cuts() ) , pid )
    def AddSignalPIDList( self , eventtype , pidlist ):
        self.AddOptionValue( 'Generation.{0}.SignalPIDList'.format( eventtype.Sample() ) ,
                          '{0} {1} {2}'.format( self.list_begin , pidlist , self.list_end ) )
    def AddInclusivePIDList( self , eventtype , pidlist ):
        self.AddOptionValue( 'Generation.{0}.InclusivePIDList'.format( eventtype.Sample() ) ,
                          '{0} {1} {2}'.format( self.list_begin ,pidlist , self.list_end ) )
    def AddFullEventCuts( self , eventtype ):
        self.AddOptionValue( 'Generation.FullGenEventCutTool' , '"{0}"'.format( eventtype.FullEventCuts() ) )
    def AddCutOptions( self , eventtype ):
        [ self.AddOptionValue( 'Generation.{0}.{1}.{2}'.format( eventtype.Sample() ,
                                                            eventtype.Cuts() ,
                                                            eventtype.CutsOptions().split()[2*i] )  ,
                                                            eventtype.CutsOptions().split()[2*i+1] , True )
        for i in range( len(eventtype.CutsOptions().split())/2 ) ]
    def AddDecayOptions( self , eventtype ):
        [ self.AddOptionValue( 'ToolSvc.{0}Decay.{1}'.format( eventtype.DecayEngine() ,
                                                              eventtype.DecayOptions().split()[2*i] )  ,
                               eventtype.DecayOptions().split()[2*i+1] )
        for i in range( len(eventtype.DecayOptions().split())/2 ) ]
    def AddDecayEngine( self , eventtype ):
        self.AddOptionValue( 'ToolSvc.{0}Decay.UserDecayFile'.format( eventtype.DecayEngine() ) ,
                          '"$DECFILESROOT/dkfiles/{0}.dec"'.format( eventtype.DecayName() ) )
        self.AddOptionValue( 'Generation.DecayTool' , '"{0}Decay"'.format( eventtype.DecayEngine() ) )
        self.AddOptionValue( 'Generation.{0}.DecayTool'.format( eventtype.Sample() ) ,
                             '"{0}Decay"'.format( eventtype.DecayEngine() ) )
    def AddRarePileUpTool( self ):
        self.AddOptionValue( 'Generation.PileUpTool' , '"FixedLuminosityForRareProcess"' )


class TextOptionFile( GenericOptionFile ):
    comment = "//"
    suffix = ".opts"
    true_string = "true"
    list_begin = "{"
    list_end   = "}"
    def AddOptionValue( self , option , value , substitute = False ):
        self.Write( [ "{0} = {1};".format( option , value ) ] )
    def AddInclude( self , filename ):
        self.Write( [ '#include \"$DECFILESROOT/options/{0}.opts\"'.format( filename ) ] )
    def IncreaseOptionValue( self , option , value ):
        self.Write( [ "{0} += {1};".format( option , value ) ] )

class PythonOptionFile( GenericOptionFile ):
    comment = "#"
    suffix = ".py"
    true_string = "True"
    list_begin = "["
    list_end   = "]"
    def __init__( self ):
        self.list_algorithm = []
        self.list_tool = []
        super( PythonOptionFile , self ).__init__()
    def ConfigureToolAndAlgo( self , option ):
        list_of_option = option.split('.')
        algo = list_of_option[0]
        if algo not in self.list_algorithm:
            self.list_algorithm.append( algo )
            self.Write( [ "from Configurables import {0}".format( algo ) ] )
        tool = []
        for op in range(1,len(list_of_option)-1):
            tool.append( ( list_of_option[ op ] , option.split( list_of_option[ op ] )[0].rstrip('.') ) )
        new_tools = [ t for t in tool if t not in self.list_tool ]
        for new_tool in new_tools:
            self.list_tool.append( new_tool )
            self.Write( [ "from Configurables import {0}".format( new_tool[0] ) ,
                          "{0}.addTool( {1} )".format( new_tool[1].replace( algo , "{0}()".format( algo ) ) , new_tool[0] ) ] )
        return option.replace( algo , "{0}()".format( algo ) , 1 )
    def AddOptionValue( self , option , value , substitute = False ):
        option = self.ConfigureToolAndAlgo( option )
        value = value.replace( '{' , '[' )
        value = value.replace( '}' , ']' )
        if substitute:
            value = value.replace( 'true' , 'True' )
            value = value.replace( 'false' , 'False' )
            if 'GeV' in value:
                self.Write( [ 'from GaudiKernel import SystemOfUnits' ] )
                value = value.replace( 'GeV' , 'SystemOfUnits.GeV' )
            if 'MeV' in value:
                self.Write( [ 'from GaudiKernel import SystemOfUnits' ] )
                value = value.replace( 'MeV' , 'SystemOfUnits.MeV' )
        self.Write( [ "{0} = {1}".format( option , value ) ] )
    def IncreaseOptionValue( self , option , value ):
        option = self.ConfigureToolAndAlgo( option )
        self.Write( [ "{0} += {1}".format( option , value ) ] )
    def AddInclude( self , filename ):
        self.Write( [ 'from Gaudi.Configuration import *' , 'importOptions( \"$DECFILESROOT/options/{0}.py\" )'.format( filename ) ] )
    def AddPGunInfo( self, pdgIDs, eventtype ):
        pdgIDsSplit = pdgIDs.split(',')
        self.Write( [ '',
                      '# Ad-hoc particle gun code',
                      '',
                      'from Configurables import ParticleGun',
                      'pgun = ParticleGun("ParticleGun")',
                      'pgun.SignalPdgCode = {0}'.format( pdgIDsSplit[0] ),
                      'pgun.DecayTool = "EvtGenDecay"',
                      'pgun.GenCutTool = "DaughtersInLHCb"',
                      '' ,
                      'from Configurables import FlatNParticles',
                      'pgun.NumberOfParticlesTool = "FlatNParticles"',
                      'pgun.addTool( FlatNParticles , name = "FlatNParticles" )',
                      '' ,
                      'from Configurables import MomentumSpectrum',
                      'pgun.ParticleGunTool = "MomentumSpectrum"',
                      'pgun.addTool( MomentumSpectrum , name = "MomentumSpectrum" )',
                      'pgun.MomentumSpectrum.PdgCodes = [ {0} ]'.format( pdgIDs ),
                      'pgun.MomentumSpectrum.InputFile = "$PGUNSDATAROOT/data/Ebeam4000GeV/MomentumSpectrum_{0}.root"'.format( pdgIDsSplit[0] ),
                      'pgun.MomentumSpectrum.BinningVariables = "{0}"'.format( pGunMomentumFileIDs[int(pdgIDsSplit[0])][0] ),
                      'pgun.MomentumSpectrum.HistogramPath = "{0}"'.format( pGunMomentumFileIDs[int(pdgIDsSplit[0])][1] ),
                      '',
                      'from Configurables import BeamSpotSmearVertex',
                      'pgun.addTool(BeamSpotSmearVertex, name="BeamSpotSmearVertex")',
                      'pgun.VertexSmearingTool = "BeamSpotSmearVertex"',
                      'pgun.EventType = {0}'.format( eventtype ) ] )

class EventType:
    """ Class to hold event type information
    """

    MandatoryKeywords = [ 'EventType' , 'Descriptor' , 'NickName' , 'Cuts' ,
                          'Documentation' , 'PhysicsWG' , 'Tested' , 'Responsible' ,
                          'Email' , 'Date' ]
    OptionalKeywords = [ 'Sample' , 'ExtraOptions' , 'DecayOptions' ,
                        'DecayEngine' , 'CutsOptions' , 'Configuration' , 'ParticleType' ,
                        'Momentum' , 'MomentumRange' , 'Id' , 'Production' ,
                        'FullEventCuts' , 'ParticleValue' , 'ParticleTable' ,
                        'SUSYModel' , 'PolarizedLambdab'  , 'InsertPythonCode' , 'CPUTime' ]
    def __init__( self , filename , remove , technology ):
        """ filename is the name of the decay file
            remove is set to yes to force removing the option file and create a new one
            technology is Text for text option file and Python for python options
        """
        self.DecayFileName = os.path.normpath( filename )
        self.KeywordDictionary = { }
        self.remove = remove
        self.OptionFile = None
        self.technology = technology

    def DecodeDecayFile( self ):
        fullstring = ''
        with open( self.DecayFileName , 'rb' ) as f:
            for line in f:
                # Keep only lines starting with '#'
                if line.startswith('# '):
                    line = line.replace( '# ', '' , 1 )
                    fullstring += line
                elif line.startswith('#'):
                    line = line.lstrip('#')
                    fullstring += line

        pattern1 = r'(?m)(\w+): (.+)'
        pattern2 = r'(Documentation):((?s).*)EndDocumentation'
        pattern3 = r'(InsertPythonCode):((?s).*)EndInsertPythonCode'
        matchObj1 = re.findall( pattern1 , fullstring )
        matchObj2 = re.findall( pattern2 , fullstring )
        matchObj3 = re.findall( pattern3 , fullstring )
        if matchObj1 or matchObj2 or matchObj3:
            for matchobj in matchObj1 + matchObj2 + matchObj3:
                self.KeywordDictionary[ matchobj[0] ] = matchobj[1]
        keystodelete = [ ]
        # delete keys found if Python Code
        if matchObj3:
            matchObj = re.findall( pattern1 , self.KeywordDictionary[ 'InsertPythonCode' ] )
            if matchObj:
                for matchobj in matchObj:
                    keystodelete.append( matchobj[0] )
        # remove leading and ending spaces, except for python code
        for k , v in self.KeywordDictionary.iteritems():
            if k != 'InsertPythonCode':
                self.KeywordDictionary[ k ] = v.rstrip(' \n').lstrip(' \n')
                if self.KeywordDictionary[ k ] == '':
                    keystodelete.append( k )
        for k in keystodelete:
            del self.KeywordDictionary[ k ]

    def Validate( self , obsoletes ):
        # check for the presence of mandatory keywords
        missing_mandatory = set( self.MandatoryKeywords ) - set( self.KeywordDictionary.keys() )
        if len( missing_mandatory ) != 0:
            logging.error( "%s.dec is missing mandatory keywords: %s" , self.DecayName() , [ key for key in missing_mandatory ] )
            raise SyntaxWarning
        unknown_keywords = set( self.KeywordDictionary.keys() ) - ( set( self.MandatoryKeywords ) | set( self.OptionalKeywords ) )
        if len( unknown_keywords ) != 0:
            logging.error( "%s.dec contains unknown keywords: %s" , self.DecayName() , [ key for key in unknown_keywords ] )
            raise SyntaxWarning

        # check if the nickname is correct
        if self.NickName() != self.DecayName():
            logging.error( "In %s, the nickname %s is not equal to the name of the file %s." , self.DecayFileName ,
                          self.KeywordDictionary[ 'NickName' ] , self.DecayName() )
            raise UserWarning

        # check if the date format is correct
        try:
            thetime = time.strptime( self.Date() , "%Y%m%d" )
        except ValueError:
            logging.error( "In %s, the date format is not correct, it should be YYYYMMDD instead of %s.",
                           self.DecayFileName , self.Date() )
            raise UserWarning

        # check physics wg name
        if self.PhysicsWG() not in list_of_wg:
            logging.error( "In %s, the name of the WG is not correct: %s.",
                           self.DecayFileName , self.PhysicsWG() )

        # check the event type does not start with 0
        if self.EventTypeNumber()[0] == '0':
            logging.error( "The EventType is not correct in %s." , self.DecayFileName )
            logging.error( "It cannot start with 0." )
            raise UserWarning

        # check the event type has at least 8 digits
        if len(self.EventTypeNumber()) < 8:
            logging.error( "The EventType is not correct in %s." , self.DecayFileName )
            logging.error( "It must have at least 8 digits." )
            raise UserWarning

        # check if the event is obsolete
        if self.EventTypeNumber() in obsoletes:
            logging.error( "The EventType %s is in use in the obsolete list, please change it." , self.EventTypeNumber() )
            raise UserWarning

        # check Tested is equal to Yes or No
        self.KeywordDictionary[ 'Tested' ] = self.KeywordDictionary[ 'Tested' ].lower()
        if self.KeywordDictionary[ 'Tested' ] != 'yes' and self.KeywordDictionary[ 'Tested' ] != 'no':
            logging.error( "In %s, Tested should be equal to Yes or No" , self.DecayName() )
            raise UserWarning

        # check that the file has been tested (check can be disabled with --force option)
        if self.KeywordDictionary[ 'Tested' ] == 'no':
            logging.error( "The decay file %s has not been tested" , self.DecayName() )
            raise SyntaxWarning

    def EventTypeNumber( self ):
        return self.KeywordDictionary[ 'EventType' ].replace(' ' , '' )
    def G( self ):
        return self.EventTypeNumber()[ 0 ]
    def S( self ):
        return self.EventTypeNumber()[ 1 ]
    def D( self ):
        return self.EventTypeNumber()[ 2 ]
    def C( self ):
        return self.EventTypeNumber()[ 3 ]
    def N( self ):
        return self.EventTypeNumber()[ 4 ]
    def T( self ):
        return self.EventTypeNumber()[ 5 ]
    def X( self ):
        return self.EventTypeNumber()[ 6 ]
    def U( self ):
        return self.EventTypeNumber()[ 7 ]


    def IsParticleGun( self ):
        return ( self.EventTypeNumber()[0] == '5' )
    def IsSpecialSource( self ):
        return ( ( self.EventTypeNumber()[0] == '6' and self.EventTypeNumber()[3] == '5' ) or
                ( self.EventTypeNumber()[0] == '6' and self.EventTypeNumber()[3] == '4' ) )
    def IsBeamGas( self ):
        return ( ( self.EventTypeNumber()[0] == '6' and self.EventTypeNumber()[3] == '0' ) or
                ( self.EventTypeNumber()[0] == '6' and self.EventTypeNumber()[3] == '1' ) )
    def IsSUSY( self ):
        return ( ( self.EventTypeNumber()[0:2] == '45' ) or ( self.EventTypeNumber()[0:2] == '46' ) )
    def SetOptionFileName( self , filename = None ):
        if "Text" in self.technology:
            self.OptionFile = TextOptionFile( )
        else:
            self.OptionFile = PythonOptionFile( )

        if not filename:
            filename = "{0}/options/{1}".format( os.environ['DECFILESROOT'] , self.EventTypeNumber() )
        self.OptionFile.SetFileName( filename )
        if os.path.exists( self.OptionFile.OptionFileName() ):
            if self.remove:
                os.remove( self.OptionFile.OptionFileName() )
            else:
                logging.warning( "The file %s already exists." , self.OptionFile.OptionFileName() )
                logging.warning( "To overwrite it, you should remove it first or run with the --remove option." )
                raise UserWarning
        self.OptionFile.Open( )

    def DecayDescriptor( self ):
        return self.KeywordDictionary[ 'Descriptor' ]
    def HasPythonCodeToInsert( self ):
        return 'InsertPythonCode' in self.KeywordDictionary.keys()
    def PythonCodeToInsert( self ):
        return self.KeywordDictionary[ 'InsertPythonCode' ]
    def HasPolarizedLambdab( self ):
        return 'PolarizedLambdab' in self.KeywordDictionary.keys()
    def PolarizedLambdab( self ):
        return self.KeywordDictionary[ 'PolarizedLambdab' ].lower()
    def HasExtraOptions( self ):
        return 'ExtraOptions' in self.KeywordDictionary.keys()
    def ExtraOptions( self ):
        return self.KeywordDictionary[ 'ExtraOptions' ]
    def HasDecayEngine( self ):
        return 'DecayEngine' in self.KeywordDictionary.keys()
    def DecayEngine( self ):
        return self.KeywordDictionary[ 'DecayEngine' ]
    def HasCuts( self ):
        return 'Cuts' in self.KeywordDictionary.keys()
    def Cuts( self ):
        return self.KeywordDictionary[ 'Cuts' ]
    def HasCutsOptions( self ):
        return 'CutsOptions' in self.KeywordDictionary.keys()
    def CutsOptions( self ):
        return self.KeywordDictionary[ 'CutsOptions' ]
    def HasDecayOptions( self ):
        return 'DecayOptions' in self.KeywordDictionary.keys()
    def DecayOptions( self ):
        return self.KeywordDictionary[ 'DecayOptions' ]
    def HasFullEventCuts( self ):
        return 'FullEventCuts' in self.KeywordDictionary.keys()
    def FullEventCuts( self ):
        return self.KeywordDictionary[ 'FullEventCuts' ]
    def HasParticleTable( self ):
        return 'ParticleTable' in self.KeywordDictionary.keys()
    def ParticleTable( self ):
        return self.KeywordDictionary[ 'ParticleTable' ]
    def HasParticleValue( self ):
        return 'ParticleValue' in self.KeywordDictionary.keys()
    def ParticleValue( self ):
        return self.KeywordDictionary[ 'ParticleValue' ]
    def HasSUSYModel( self ):
        return 'SUSYModel' in self.KeywordDictionary.keys()
    def SUSYModel( self ):
        return self.KeywordDictionary[ 'SUSYModel' ].split()
    def HasConfiguration( self ):
        return 'Configuration' in self.KeywordDictionary.keys()
    def Configuration( self ):
        return self.KeywordDictionary[ 'Configuration' ].split()
    def HasParticleType( self ):
        return 'ParticleType' in self.KeywordDictionary.keys()
    def ParticleType( self ):
        return self.KeywordDictionary[ 'ParticleType' ].split()
    def HasMomentum( self ):
        return 'Momentum' in self.KeywordDictionary.keys()
    def Momentum( self ):
        return self.KeywordDictionary[ 'Momentum' ].split()
    def HasMomentumRange( self ):
        return 'MomentumRange' in self.KeywordDictionary.keys()
    def MomentumRange( self ):
        return self.KeywordDictionary[ 'MomentumRange' ].split()
    def NickName( self ):
        return self.KeywordDictionary[ 'NickName' ].replace( ' ' , '' )
    def Date( self ):
        return self.KeywordDictionary[ 'Date' ]
    def PhysicsWG( self ):
        return self.KeywordDictionary[ 'PhysicsWG' ]

    def DecayName(self):
        return os.path.splitext( os.path.split( self.DecayFileName )[ 1 ] )[ 0 ]

    def Sample( self ):
        # Check if overriden
        if 'Sample' in self.KeywordDictionary.keys():
            return self.KeywordDictionary['Sample']
        sample = "otherTreatment"
        if self.EventTypeNumber()[0:2] == '30':
            sample = "MinimumBias"
        elif int(self.EventTypeNumber()[0]) in (1, 2, 3, 7):
            if int(self.EventTypeNumber()[1]) in (0, 9):
                sample = "Inclusive"
            elif self.EventTypeNumber()[0:2] == '31' :  ## signal tau production
                sample = "SignalPlain"
            elif self.EventTypeNumber()[0:2] == '32': ## Sigma+ production
                sample = "SignalPlain"
            elif self.EventTypeNumber()[0:2] == '33': ## Lambda production
                sample = "SignalPlain"
            elif self.EventTypeNumber()[0:2] == '34': ## K0S production
                sample = "SignalPlain"
            elif self.EventTypeNumber()[0:2] == '35': ## Xi- production
                sample = "SignalPlain"
            elif self.EventTypeNumber()[0:2] == '36': ## Omega- production
                sample = "SignalPlain"
            elif self.EventTypeNumber()[0:2] == '37': ## K production
                sample = "SignalPlain"
            elif self.EventTypeNumber()[0:2] == '38': ## K0L production
                sample = "SignalPlain"
            elif int(self.EventTypeNumber()[0]) == 1 and int(self.EventTypeNumber()[1]) in (1, 2, 3, 6, 7):
                sample = "SignalRepeatedHadronization"
            elif int(self.EventTypeNumber()[0]) == 1 and int(self.EventTypeNumber()[1]) == 5:
                sample = "SignalPlain"
            elif int(self.EventTypeNumber()[0]) == 2 and int(self.EventTypeNumber()[1]) == 8 and int(self.EventTypeNumber()[6]) == 1:
                sample = "Special"
            elif int(self.EventTypeNumber()[0]) in (2, 7) and int(self.EventTypeNumber()[1]) in (1, 2, 3, 4, 5, 7, 8):
                sample = "SignalPlain"
            elif int(self.EventTypeNumber()[0]) == 1 and int(self.EventTypeNumber()[1]) == 8:
                # bb resonance: use Special
                sample = "Special"
            elif int(self.EventTypeNumber()[0]) == 1 and int(self.EventTypeNumber()[1]) == 4:
                # SignalForcedFragmentation
                sample = "SignalForcedFragmentation"
                # Check production
                if 'Production' in self.KeywordDictionary.keys():
                    BcProductionValue = self.KeywordDictionary['Production']
                    if BcProductionValue == "BcVegPy":
                        sample = "Special"
            elif int(self.EventTypeNumber()[0]) == 2 and int(self.EventTypeNumber()[1]) == 6:
                # Check production
                if 'Production' in self.KeywordDictionary.keys(): ## For Xicc decay
                    XiccProductionValue = self.KeywordDictionary['Production']
                    if XiccProductionValue == "GenXicc":
                        sample = "Special"
                else:
                    sample = "SignalPlain"
        elif int(self.EventTypeNumber()[0]) == 4 and ( (int(self.EventTypeNumber()[1]) in range(7)) or  (int(self.EventTypeNumber()[1])==9)):
            sample = "Special"
        elif self.EventTypeNumber()[0] == '6':
            sample = "MinimumBias"
        return sample

    def Production( self ):
        production = 'Pythia'
        if "Production" in self.KeywordDictionary.keys():
            production = self.KeywordDictionary[ 'Production' ]
        return production

    def HeaderOptions( self ):
        """  write the header of the options file
        """
        self.OptionFile.WriteHeader( self.EventTypeNumber() , self.DecayDescriptor() )

# ============================================================================================
def susyOptions( eventtype ):
    """ Utility function for SUSY model: only for G=4, S=5,6
    """

    if not eventtype.HasSUSYModel():
        logging.error( "No SUSY Model Keyword defined" )
        raise UserWarning

    optValues = eventtype.SUSYModel()
    if len(optValues) != 1 and len(optValues) != 2 :
        logging.error( "The Keyword SUSY must have one or two values: Model and Option (eg. Kaplan_hkk 10ps)" )
        raise UserWarning

    model = optValues[0]
    choice = model

    if len( optValues ) == 2: choice = choice+'_'+optValues[1]

    # include main options for the model: Kaplan or SusyBRpV
    extra = ''
    if eventtype.S() == '5':
        extra = 'Kaplan'
    elif eventtype.S() == '6':
        extra = 'SusyBRpV'

    eventtype.OptionFile.AddInclude( extra )

    if eventtype.S() == '5':
        eventtype.OptionFile.AddInclude( model )
        eventtype.OptionFile.AddOptionValue( "Generation.Special.PythiaProduction.SLHADecayFile" ,
                                             '"{0}.LHdec"'.format( choice ) )
        eventtype.OptionFile.AddOptionValue( "Generation.Special.PythiaProduction.PDecayList" ,
                                            "{1000022}" )
    elif eventtype.S() == '6':
        eventtype.OptionFile.AddOptionValue( "Generation.Special.PythiaProduction.SLHASpectrumFile" ,
                                            '"{0}.LHspc"'.format( choice ) )
        if 'AMSB' in optValues[0]:
            eventtype.OptionFile.AddOptionValue( "Generation.Special.PythiaLSP.LSPID" ,
                                                 "{ 1000022, 1000024 }" )

def beamGasLssArcToolsOptions( iev , eventtype ):
    """ Utility function for Halo from beam gas interactions in LSS and arc
    """

    # Find all particles to do: Muons, Hadrons or both
    pType, cConf, bConf = iev[1], iev[2], iev[4]
    pTypes = []

    if (pType != '0' and pType != '2' and pType != '9'):
        logging.error( "Only value 0(all), 2(muons), 9(hadrons) allowed in ParticleTypes" )
        raise UserWarning
    else:
        if (pType == '2' or pType == '0'):
            pTypes.append('Muons')
        if (pType == '9' or pType == '0'):
            pTypes.append('Hadrons')

    # Find machine conditions
    iConf = int(cConf)
    if (iConf < 0 or iConf > 2):
        logging.error( 'Only value from 0 to 2 allowed in Configuration' )
        raise UserWarning
    sDict = { 0:'Beta10Startup' , 1:'Beta01Startup', 2:'Beta10Scrubbed' }
    source = sDict[iConf]

    # Find beam
    if (bConf != '0' and bConf != '1' and bConf != '2'):
        logging.error( 'Only value from 0 to 2 allowed as Beam type' )
        raise UserWarning
    beams = []
    if (bConf == '0' or bConf == '1'):
        beams.append('Beam1')
    if (bConf == '0' or bConf == '2'):
        beams.append('Beam2')

    # Write all options for the tool to use (may be from 1 to 4)
    pDict = { 'Muons':'mu', 'Hadrons':'h' }

    nickBeam = ''
    for b in beams:
        nickBeam += b
        nickPType = ''
        for p in pTypes:
            nickPType += pDict[p]
            toolName = source+b+p
            eventtype.OptionFile.IncreaseOptionValue( 'MIBackground.MIBSources' , '{ "CollimatorSource/%s" }' % toolName )
            filename = '{0}.{1}.{2}.data'.format( source , b , pDict[p] )
            eventtype.OptionFile.AddOptionValue( 'MIBackground.{0}.ParticleSourceFile'.format( toolName ) ,
                                                '\"$MIBDATAROOT/data/{0}\"'.format( filename ) )
            if b == 'Beam2':
                eventtype.OptionFile.AddOptionValue( 'MIBackground.{0}.ZParticleOrigin'.format( toolName ) , '19.9*m' )
                eventtype.OptionFile.AddOptionValue( 'MIBackground.{0}.ZDirection'.format( toolName ) , '-1' )

    nickTxt = '.{0}.{1}.{2}'.format( nickBeam , source , nickPType )
    return nickTxt

def tctHaloToolsOptions( iev , eventtype ):
    """ Utility function for Halo on Collimators
    """

    # Find all particles to do: Muons, Hadrons or both
    pType = iev[1]
    cConf = iev[2]
    pTypes = []
    if (pType != '0' and pType != '2' and pType != '9'):
        logging.error( 'Only value 0(all), 2(muons), 9(hadrons) allowed in ParticleTypes' )
        raise UserWarning
    else:
        if (pType == '2' or pType == '0'):
            pTypes.append('Muons')
        if (pType == '9' or pType == '0'):
            pTypes.append('Hadrons')

    # Find Shield configuration to use (only one possible!)
    iConf = int(cConf)
    if (iConf < 0 or iConf > 8):
        logging.error( 'Only value from 0 to 8 allowed in Configuration' )
        raise UserWarning
    sDict = {0:'StagedShield', 1:'Shield', 2:'NoShield'}
    ishield = (iConf)/3
    shield = sDict[ishield]

    # Find Collimator source to use (TCTV, TCTH or both)
    tct = (iConf)%3
    tctList = []
    if( tct == 0 or tct == 1 ):
        tctList.append('TCTV')
    if( tct == 0 or tct == 2 ):
        tctList.append('TCTH')

    # Write all options for the tool to use (may be from 1 to 4)
    pDict = { 'Muons':'mu', 'Hadrons':'h' }
    sDict = { 'StagedShield':'staged_shield', 'Shield':'shield', 'NoShield':'no_shield'}

    nickTCT = ''
    for c in tctList:
        nickTCT += c
        nickPType = ''
        for p in pTypes:
            nickPType += pDict[p]
            toolName = c+shield+p
            eventtype.OptionFile.IncreaseOptionValue( 'MIBackground.MIBSources' ,
                                                     '{ "CollimatorSource/%s" }' % toolName )
            filename = '{0}.{1}.{2}.data'.format( c , sDict[shield] , pDict[p] )
            eventtype.OptionFile.AddOptionValue( 'MIBackground.{0}.ParticleSourceFile'.format( toolName ) ,
                                                '"$MIBDATAROOT/data/{0}"'.format( filename ) )

    nickTxt = '.{0}.{1}.{2}'.format( nickTCT , sDict[shield] , nickPType )
    return nickTxt

def beamHalo( eventtype ):
    """ Options for Halo on Collimators
    EventType = GSDCTNXU, G=6 & C=5 halo on collimators
    S = particle types generated (similar as for G=5)
          0: all
          2: mu
          9: other (i.e. hadrons)
    D = special meaning of source configuration (shield and collimator)
          0: staged shield - Loss on TCTV.4L8.B1 & TCTH.L8.B1
          1: staged shield - Loss on TCTV.4L8.B1
          2: staged shield - Loss on TCTH.L8.B1
          3: design shield - Loss on TCTV.4L8.B1 & TCTH.L8.B1
          4: design shield - Loss on TCTV.4L8.B1
          5: design shield - Loss on TCTH.L8.B1
          6: no shield - Loss on TCTV.4L8.B1 & TCTH.L8.B1
          7: no shield - Loss on TCTH.L8.B1
          8: no shield - Loss on TCTH.L8.B1
    T=0: both beams, T=1: beam1, T=2: beam2
    N=Num. of bunches traveling (beam1), X=Num. of bunches traveling (beam2)

    EventType = GSDCTNXU, G=6 & C=4 halo from LSS and arc beam gas
    S = particle types generated (similar as for G=5)
          0: all
          2: mu
          9: other (i.e. hadrons)
    D = special meaning of source configuration (Gas densities and beam beta*)
          0: Startup gas pressure, Beta* = 10m
          1: Startup gas pressure, Beta* = 1m
          2: Scrubbed gas pressure, Beta* = 10m
    T=0: both beams, T=1: beam1, T=2: beam2
    """

    # If mirror Keyword is present duplicate options as controlled
    # otherwise use eventtype as-is
    ptypeValue = eventtype.ParticleType()
    G = eventtype.G()
    CTNXU = eventtype.EventTypeNumber()[3:8]
    eventList = []
    if (eventtype.HasConfiguration()):
        configList = eventtype.Configuration()
    else:
        configList = [eventtype.S()]

    if (eventtype.HasParticleType()):
        ptypeList = eventtype.ParticleType()
    else:
        ptypeList = [eventtype.D()]

    for iconf in configList:
        for ipart in ptypeList:
            eventList.append(G+ipart+iconf+CTNXU)

    # Now loop over list of event Type and write the options
    for iev in eventList:
        optionsFile = '{0}/options/{1}'.format( os.environ['DECFILESROOT'] , iev )
        eventtype.SetOptionFileName( optionsFile )
        eventtype.HeaderOptions( )
        eventtype.OptionFile.AddOptionValue( 'GaussGen.PrintFreq' , 100 )
        eventtype.OptionFile.AddOptionValue( 'GaussSim.PrintFreq' , 100 )
        eventtype.OptionFile.AddOptionValue( 'GiGaGetEventAlg.OutputLevel' , 4 )
        if eventtype.HasExtraOptions():
            eventtype.OptionFile.AddExtraOptions( eventtype )

        if iev[3] == '4':
            nickTxt = beamGasLssArcToolsOptions( iev , eventtype )
        elif iev[3] == '5':
            nickTxt = tctHaloToolsOptions( iev , eventtype )
        else:
            logging.error( 'Only value 4(Beam Gas LSS) and 5(TCT Halo) allowed as source' )
            raise UserWarning
        eventtype.OptionFile.AddOptionValue( 'MIBackground.EventType' , '{0}'.format( iev ) )
        evtNick = eventtype.NickName()+nickTxt
        writeBkkTable( iev , eventtype.DecayDescriptor() , evtNick )
        writeSQLTable( iev , eventtype.DecayDescriptor() , evtNick )

def beamGasLHCb( eventtype ):
    """ Options for Beam gas
    """

    Znuclei = [1,  6,  8, 10, 18, 36,  54]
    Anuclei = [1, 12, 16, 20, 40, 84, 131]

    # get the last digits of the event type and check that the event type
    # is providing all necessary info
    NXU = eventtype.EventTypeNumber()[5:8]
    if eventtype.EventTypeNumber()[6:8] == '00':
        logging.error( "Atomic Number not provided" )
        raise UserWarning

    data = '[\n "hijinginit frame LAB",\n'

    # Check that the atomic number is in the list
    atomicNum=int(NXU)

    if atomicNum not in Znuclei:
        logging.error( 'Atomic Number not allowed ( NUX != {d} )'.format( Znuclei ) )
        raise UserWarning

    if atomicNum!=1:
        data += '  "hijinginit targ A",\n'
    else:
        data += '  "hijinginit targ P",\n'

    beam = int(eventtype.N())

    if not (beam in range(0,3)):
        logging.error( 'beam number not allowed (T can be only 0,1,2)' )
        raise UserWarning

    if beam==0:
        beam=beam+12
    massNum = Anuclei[Znuclei.index(atomicNum)]
    data += '  "hijinginit beam{0:d}",\n'.format( beam )
    data += '  "hijinginit iat {0:d}",\n'.format( massNum )
    data += '  "hijinginit izt {0:d}"\n'.format( atomicNum )
    data += ']'

    eventtype.OptionFile.IncreaseOptionValue( 'Generation.MinimumBias.HijingProduction.Commands',
                                             data )

    # set time of interaction, for event with both beam set it to zero
    if beam==12: beam=0
    elif beam==2: beam=-1

    eventtype.OptionFile.AddOptionValue( 'Generation.FlatZSmearVertex.BeamDirection' , str(beam) )
    eventtype.OptionFile.AddOptionValue( 'Generation.UniformSmearVertex.BeamDirection' , str(beam) )

def genParticleGuns( eventtype ):
    """ Options for particle guns
    """

    if not eventtype.HasMomentum() and not eventtype.HasMomentumRange():
        logging.error( 'There is no correct value for the keyword Momentum in %s.dec' ,
                      eventtype.DecayName() )
        raise UserWarning

    if eventtype.HasMomentum():
        momentumValues = eventtype.Momentum()
    else:
        momentumValues = eventtype.MomentumRange()

    # Check in case of range that only two values are given
    if eventtype.HasMomentumRange():
        if len(momentumValues) != 2:
            logging.error( 'MomentumRange wants only 2 values: min and max. You have given {0}',
                          len(momentumValues))
            raise UserWarning
        if eventtype.C() not in ('4','5','6','7'):
           logging.error( 'Momentum range requested but C = {0} is not allowed.' , eventtype.EventTypeNumber()[3] )
           raise UserWarning
    else:
        if int(eventtype.C()) > 3:
            logging.error( 'Momentum fix value requested but C = {0} is not allowed.' , eventtype.EventTypeNumber()[3] )
            raise UserWarning

    ## determine absolute pID
    value = pgunPID( eventtype )

    # pGunType: acceptance, fix momentum or range, (flat eta, flat x-y,
    #                                               not implemented yet)
    acceptance, acc, gType = pGunType( int(eventtype.C() ) )

    # C = 0, 1, 2 or 3: fix list of momentum
    if gType == 1:
        for val in momentumValues:
            pGunMomentum( acc , val , val, eventtype )
            if eventtype.HasExtraOptions():
                 eventtype.OptionFile.AddInclude( eventtype.ExtraOptions() )
            eventtype.OptionFile.AddOptionValue( 'ParticleGun.ParticleGunTool' , '"MomentumRange"' )
            eventtype.OptionFile.AddOptionValue( 'ParticleGun.NumberOfParticlesTool' , '"FlatNParticles"' )
            eventtype.OptionFile.AddOptionValue( 'ParticleGun.MomentumRange.PdgCodes' , '{ %s }' % value )
            eventtype.OptionFile.AddEvtGenUserDecayFile( eventtype )
            if eventtype.HasParticleTable():
                eventtype.OptionFile.AddParticleTable( eventtype )
            if eventtype.HasParticleValue():
                eventtype.OptionFile.AddParticleValue( eventtype )
            eventtype.OptionFile.AddInclude( acceptance )
    elif gType == 2:
        pGunMomentum( acc, momentumValues[0], momentumValues[1], eventtype )
        if eventtype.HasExtraOptions():
            eventtypeOptionFile.AddInclude( eventtype.ExtraOptions() )
        eventtype.OptionFile.AddOptionValue( 'ParticleGun.ParticleGunTool' , '"MomentumRange"' )
        eventtype.OptionFile.AddOptionValue( 'ParticleGun.NumberOfParticlesTool' , '"FlatNParticles"' )
        eventtype.OptionFile.AddOptionValue( 'ParticleGun.MomentumRange.PdgCodes' , '{ %s }' % value )
        eventtype.OptionFile.AddEvtGenUserDecayFile( eventtype )
        if eventtype.HasParticleTable():
            eventtype.OptionFile.AddParticleTable( eventtype )
        if eventtype.HasParticleValue():
            eventtype.OptionFile.AddParticleValue( eventtype )
        eventtype.OptionFile.AddInclude( acceptance )
    else:
        logging.error( 'Case C >=8 for ParticleGun not implemented yet' )
        raise UserWarning

def pgunPID( eventtype ):
    """ PID, helper for particlegun
    """

    ## determine absolute pID
    if eventtype.S() == '1': value = '11'
    elif eventtype.S() == '2': value = '13'
    elif eventtype.S() == '3': value = '211'
    elif eventtype.S() == '4': value = '321'
    elif eventtype.S() == '5': value = '2212'
    elif eventtype.S() == '6': value = '22'
    elif eventtype.S() == '7': value = '111'
    elif eventtype.S() == '9': value = '0'
    else:
        logging.error( 'The EventType has S = %s not yet implemented' , eventtype.S() )
        raise UserWarning

    ## determine if particle or antiparticle or both
    if eventtype.D() == '0': value = value
    elif eventtype.D() == '1': value = '-'+value
    elif eventtype.D() == '2': value = value+', -'+value
    else:
        logging.error( "The EventType is not correct. D can only be 0, 1 or 2" )
        raise UserWarning

    ## special case of "other particle"
    if eventtype.S() == '9':
        if eventtype.D() == '0':
            value = '443'
        else:
            logging.error( 'GSD = %s not implemented yet', eventtype.EventTypeNumber()[0:3] )
            raise UserWarning

    return value

def pGunType(cValue):
    """ Decode C, i.e. acceptance, GunType( momemtum, eta...) helper for particle gun
    """

    # C = 0, 2, 4, 6 means in CaloAcceptance, while
    # C = 1, 3, 5, 7 means in TrackersAcceptance
    acceptance = ''
    acc = 0
    if cValue in (0,2,4,6):
        acceptance = "CaloAcceptance"
    elif cValue in (1,3,5,7):
        acc = 1
        acceptance = "TrackersAcceptance"
    else:
        logging.error( 'Only value 0 to 7 implemted so far' )
        raise UserWarning

    # C = 0, 1, 2 or 3: fix list of momentum
    gType = 0
    if cValue in range(4): gType = 1
    elif cValue in range(4,8): gType = 2
    else:
        logging.error( 'Case C >= 8 for ParticleGun not implemented yet' )
        raise UserWarning

    return acceptance, acc, gType

def pGunMomentum( acc , pMin, pMax, eventtype ):
    """ helper for particle gun
    """
    momentum = '%s' % pMin.split('*')[0]
    unit     = '%s' % pMin.split('*')[1]
    momentumRound = '%0.f' % float(momentum)

    momentum = '%s' % pMax.split('*')[0]
    unit     = '%s' % pMax.split('*')[1]
    momentumRound = '%0.f' % float(momentum)

    ua = 0
    if unit == 'GeV': ua = acc
    elif unit == 'MeV': ua = acc + 2
    else:
        logging.error( 'Units can only be MeV or GeV' )
        raise UserWarning

    iEventType = eventtype.EventTypeNumber()[0:3]+str(ua)+eventtype.EventTypeNumber()[4:8]
    iEventType = iEventType[0:8-len(momentumRound)]+momentumRound

    OptionsNickAux = '{0} {1}'.format( eventtype.NickName() , pMin )
    if pMax != pMin:
        OptionsNickAux += ' - %s' % pMax

    OptionsNameAux = iEventType
    filename = '{0}/options/{1}'.format( os.environ['DECFILESROOT'] , OptionsNameAux )
    eventtype.SetOptionFileName( filename )
    eventtype.HeaderOptions( )

    eventtype.OptionFile.AddOptionValue( 'ParticleGun.MomentumRange.MomentumMin' , pMin , True )
    eventtype.OptionFile.AddOptionValue( 'ParticleGun.MomentumRange.MomentumMax' , pMax , True )
    eventtype.OptionFile.AddOptionValue( 'ParticleGun.EventType' , iEventType )

    writeBkkTable(OptionsNameAux,eventtype.DecayDescriptor(),OptionsNickAux)
    writeSQLTable(OptionsNameAux,eventtype.DecayDescriptor(),OptionsNickAux)

def writeBkkTable( evttypeid , descriptor , nickname ):
    """ write the file to create the entry in the ORACLE database
    """
    global bkk_first, eventid_inbkk
    TableName = ( "{0}/doc/table_event.txt".format( os.environ["DECFILESROOT"] ) )

    if bkk_first:
        bkk_first = False
        if not os.path.exists(TableName):
            with open( TableName , 'wb' ) as f:
                line = "EventTypeID | NickName | Description\n"
                f.write( line )
        else:
            # read the file
            with open( TableName , "rb" ) as f:
                for line in f:
                    eventid_inbkk.append( line.split()[0] )

    if evttypeid not in eventid_inbkk:
        eventid_inbkk.append( evttypeid )
        nick = nickname[:255]
        desc = descriptor[:255]
        with open( TableName, 'a+' ) as f:
            line = "{0} | {1} | {2}\n".format( evttypeid , nick , desc )
            f.write( line )

def writeSQLTable(evttypeid,descriptor,nickname):
    """ write the file to create the entry in the ORACLE database
    """
    global sql_first, eventid_insql
    TableName = "{0}/doc/table_event.sql".format( os.environ["DECFILESROOT"] )

    if sql_first:
        sql_first = False
        if not os.path.exists(TableName):
            os.system( "touch " + TableName )
        else:
            # read the file
            with open( TableName , "rb" ) as f:
                for line in f:
                    eventid_insql.append( line.split()[2].strip(',' ) )

    if evttypeid not in eventid_insql:
        eventid_insql.append( evttypeid )
        nick = nickname[:255]
        desc = descriptor[:255]
        with open( TableName, 'a+' ) as f:
            line = "EVTTYPEID = {0}, DESCRIPTION = \"{1}\", PRIMARY = \"{2}\"\n".format( evttypeid , nick , desc )
            f.write( line )

def readObsoleteTypeTable( ):
    """ read the table of obsolete events
    """
    filename = "{0}/doc/table_obsolete.sql".format( os.environ["DECFILESROOT"] )
    global list_of_obsoletes
    try:
        with open( filename , "rb" ) as f:
            for line in f:
                list_of_obsoletes.append( line.split()[2].strip(',') )
    except IOError:
        logging.warning( 'No files containing obsolete event types found' )
    except IndexError:
        pass

def run_create( dkfile , remove , python , force ):
    """ create an options file corresponding to a single Decay file
    """

    global pGunMomentumFileIDs

    technology = 'Text'
    if python: technology = 'Python'

    eventtype = EventType( dkfile , remove , technology )
    eventtype.DecodeDecayFile()

    logging.info( "Creation of options file for Decay file %s.dec", eventtype.DecayName() )
    try:
        eventtype.Validate( list_of_obsoletes )
    except SyntaxWarning:
        if force:
            pass
        else:
            raise UserWarning

    # Check if EventType is 5xxxxxxxx --> particle guns
    if eventtype.IsParticleGun():
        genParticleGuns( eventtype )
        return

    # Check if EventType is special source --> MIB (6xx5xxxx)
    if eventtype.IsSpecialSource():
        beamHalo( eventtype )
        return

    #check if the options file already exist and do not overwrite it
    eventtype.SetOptionFileName()

    # get the first digit of the eventtype
    AB = eventtype.EventTypeNumber()[0:2]
    ABX = eventtype.EventTypeNumber()[0:2]+eventtype.X()
    ABU = eventtype.EventTypeNumber()[0:2]+eventtype.U()

    eventtype.HeaderOptions( )
    # Polarized Lambda_b
    ### eventtype.OptionFile
    if AB == "15":
        if eventtype.HasPolarizedLambdab():
            if eventtype.PolarizedLambdab() == "yes":
                eventtype.OptionFile.GeneratePolarizedLambdab()

    # Optional lines for all event types ---------------------------------
    # Check if exists ExtraOptions keyword
    if eventtype.HasExtraOptions():
        eventtype.OptionFile.AddExtraOptions( eventtype )

    # Mandatory lines to write -------------------------------------------
    # Event type number
    eventtype.OptionFile.AddEventTypeNumber( eventtype )

    # Sample
    eventtype.OptionFile.AddSampleTool( eventtype )

    # ProductionValue
    eventtype.OptionFile.AddProductionTool( eventtype )
    if eventtype.Production() == 'BcVegPy' or eventtype.Production() == 'GenXicc':
        eventtype.OptionFile.AddRarePileUpTool()
        if eventtype.Production() == 'GenXicc':
            eventtype.OptionFile.AddGenXiccProductionToolBaryonState( eventtype )
            eventtype.OptionFile.AddGenXiccBeamMomentum( eventtype )

    # Decay tool
    if not eventtype.HasDecayEngine():
        eventtype.OptionFile.AddEvtGenUserDecayFile( eventtype )
    else:
        eventtype.OptionFile.AddDecayEngine( eventtype )

    # Cuts
    if eventtype.HasCuts():
        CutsValue = eventtype.Cuts()
        if CutsValue != 'LHCbAcceptance':
            if CutsValue == 'None':
                CutsValue = ''
        eventtype.OptionFile.AddCutTool( eventtype , CutsValue )
        if eventtype.Production() == 'GenXicc':
            eventtype.OptionFile.AddGenXiccCutToolBaryonState( eventtype, CutsValue )

    # Lines for specific event type Beam gas in LHCb (G=6, C=0,1) ------
    if eventtype.IsBeamGas( ):
        beamGasLHCb( eventtype )

    # Optional lines depending of existing keywords ----------------------
    # Check if exists cuts option keyword
    if eventtype.HasCutsOptions():
        eventtype.OptionFile.AddCutOptions( eventtype )

    # Check if there are options for the decay tool
    if eventtype.HasDecayOptions():
        eventtype.OptionFile.AddDecayOptions( eventtype )

    # Check if exists FullEventCuts keyword
    if eventtype.HasFullEventCuts():
        eventtype.OptionFile.AddFullEventCuts( eventtype )

    ids = ''

    # Generation.SAMPLE.GENERATOR.InclusivePIDList
    # if Inclusive
    if ( 'Inclusive' in eventtype.Sample() ):
        if eventtype.G() == '1':
            pidlist = '521, -521, 511, -511, 531, -531, 541, -541, 5122, -5122, 5222, -5222, 5212, -5212, 5112, -5112, 5312, -5312, 5322, -5322, 5332, -5332, 5132, -5132, 5232, -5232'
        elif int( eventtype.G() ) in (2, 7):
            pidlist = '421, -421, 411, -411, 431, -431, 4122, -4122, 443, 4112, -4112, 4212, -4212, 4222, -4222, 4312, -4312, 4322, -4322, 4332, -4332, 4132, -4132, 4232, -4232, 100443, 441, 10441, 20443, 445, 4214, -4214, 4224, -4224, 4314, -4314, 4324, -4324, 4334, -4334, 4412, -4412, 4414,-4414, 4422, -4422, 4424, -4424, 4432, -4432, 4434, -4434, 4444, -4444, 14122, -14122,  14124, -14124, 100441'
        eventtype.OptionFile.AddInclusivePIDList( eventtype , pidlist )
    # if Type Signal
    else:
        listing = { '10':'521, -521, 511, -511, 531, -531, 541, -541, 5122, -5122, 5222, -5222, 5212, -5212, 5112, -5112, 5312, -5312, 5322, -5322, 5332, -5332, 5132, -5132, 5232, -5232'
                    , '11':'511,-511'
                    , '12':'521,-521'
                    , '13':'531,-531'
                    , '14':'541,-541'
                    , '15':'5122,-5122'
                    , '19':'521, -521, 511, -511, 531, -531, 541, -541, 5122, -5122, 5332, -5332, 5132, -5132, 5232, -5232'
                    , '20':'421, -421, 411, -411, 431, -431, 4122, -4122, 443, 4112, -4112, 4212, -4212, 4222, -4222, 4312, -4312, 4322, -4322, 4332, -4332, 4132, -4132, 4232, -4232, 100443, 441, 10441, 20443, 445, 4214, -4214, 4224, -4224, 4314, -4314, 4324, -4324, 4334, -4334, 4412, -4412, 4414,-4414, 4422, -4422, 4424, -4424, 4432, -4432, 4434, -4434, 4444, -4444, 14122, -14122,  14124, -14124, 100441'
                    , '21':'411,-411'
                    , '22':'421,-421'
                    , '23':'431,-431'
                    , '24':'443'
                    , '25':'4122,-4122'
                    # tau
                    , '31':'15,-15'
                    # Sigma
                    , '32':'3222,-3222'
                    # Lambda
                    , '33':'3122,-3122'
                    # Ks
                    , '34':'310'
                    # Xi
                    , '35':'3312,-3312'
                    # Omega
                    , '36':'3334,-3334'
                    # K
                    , '37':'321,-321'
                    # Kl
                    , '38':'130'
                    , '70':'421, -421, 411, -411, 431, -431, 4122, -4122, 443, 4112, -4112, 4212, -4212, 4222, -4222, 4312, -4312, 4322, -4322, 4332, -4332, 4132, -4132, 4232, -4232, 100443, 441, 10441, 20443, 445, 4214, -4214, 4224, -4224, 4314, -4314, 4324, -4324, 4334, -4334, 4412, -4412, 4414,-4414, 4422, -4422, 4424, -4424, 4432, -4432, 4434, -4434, 4444, -4444, 14122, -14122,  14124, -14124, 100441'
                    , '71':'411,-411'
                    , '72':'421,-421'
                    , '73':'431,-431'
                    , '74':'443'
                    , '75':'4122,-4122'
                   }
        listingExcited = { '270':   '413,-413'
                           , '271': '423,-423'
                           , '272': '433,-433'
                           , '273': '435,-435'
                           , '274': '425,-425'
                           , '275': '415,-415'
                           , '276': '10433,-10433'
                           , '277': '413,-413'
                           , '260':'4112,-4112'
                           , '262':'4222,-4222'
                           , '263': '4114,-4114'
                           , '264': '4224,-4224'
                           , '267': '4214,-4214' ## Sigma_c*+ and Sigma_c*~-
                           , '268': '4132,-4132'
                           , '269': '4232,-4232'
                           , '770': '413,-413'
                           , '771': '423,-423'
                           , '772': '433,-433'
                           , '280': '100443'
                           , '281': '9920443'
                           , '282': '10443'
                           , '283': '10441'
                           , '284': '20443'
                           , '285': '445'
                           , '286': '441'
                           , '287': '30443'
                           , '180': '553'
                           , '181': '100553'
                           , '182': '200553'
                           , '183': '300553'
                           , '184': '9000553'
                           , '185': '10551'
                           , '186': '20553'
                           , '187': '555'
                           , '160': '5112,-5112'
                           , '161': '5212,-5212'
                           , '162': '5222,-5222'
                           , '163': '5132,-5132'
                           , '164': '5232,-5232'
                           , '165': '5332,-5332'
                           , '170': '513,-513'
                           , '171': '523,-523'
                           , '172': '533,-533'
                           , '173': '10513,-10513'
                           , '174': '10523,-10523'
                           , '175': '10533,-10533'
                           , '176': '515,-515'
                           , '177': '525,-525'
                           , '178': '535,-535'}

        if listing.has_key(AB):
            if eventtype.Sample() != "Special":
                ids = listing[AB]
                eventtype.OptionFile.AddSignalPIDList( eventtype , listing[AB] )
        elif listingExcited.has_key(ABX):
            ids = listingExcited[ABX]
            if AB=='18':
                if 'None' != eventtype.Cuts():
                    eventtype.OptionFile.AddSignalPID( eventtype , listingExcited[ ABX ] )
            elif ABX=='281':
                if 'None' != eventtype.Cuts():
                    eventtype.OptionFile.AddSignalPID( eventtype , listingExcited[ ABX ] )
            else:
                if eventtype.Sample() != "Special":
                    eventtype.OptionFile.AddSignalPIDList( eventtype , listingExcited[ ABX ] )



    # Check if exists ParticleTable keyword
    if eventtype.HasParticleTable():
        eventtype.OptionFile.AddParticleTable( eventtype )

    # Check if exists ParticleValue keyword
    if eventtype.HasParticleValue():
        eventtype.OptionFile.AddParticleValue( eventtype )

    # Check if exist Model keyword (only applicable for G=4, S=5,6)
    if eventtype.IsSUSY():
        arg = susyOptions( eventtype )

    # insert python lines directly
    if technology == 'Python':
        if eventtype.HasPythonCodeToInsert():
            eventtype.OptionFile.Write( [ eventtype.PythonCodeToInsert() ] )

    if ids and int(ids.split(',')[0]) in pGunMomentumFileIDs:
        eventtype.OptionFile.AddPGunInfo(ids, eventtype.EventTypeNumber())

    writeBkkTable( eventtype.EventTypeNumber() , eventtype.DecayDescriptor() , eventtype.NickName() )
    writeSQLTable( eventtype.EventTypeNumber() , eventtype.DecayDescriptor() , eventtype.NickName() )

def run_loop( remove , python , force ):
    """ loop in the DKFILES directory to generate the options file
    """
    files = glob.glob(os.environ["DECFILESROOT"]+"/dkfiles/*.dec")
    for f in files:
        try:
            run_create( f , remove , python , force )
        except UserWarning:
            pass

def CheckFile( option , opt_str , value , parser ):
    """ Check if file exists
    """
    if not os.path.exists( '{0}/dkfiles/{1}.dec'.format( os.environ['DECFILESROOT'] , value ) ):
        raise OptionValueError( "Decay file %s.dec " % value + "does not " +
                               "exist in the $DECFILESROOT/dkfiles " +
                               "directory" )
    setattr( parser.values , option.dest  , value )

# ---------------------------------------------------------------------------
# Color formatting
# ---------------------------------------------------------------------------
BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

#The background is set with 40 plus the number of the color, and the foreground with 30

#These are the sequences need to get colored ouput
RESET_SEQ = "\033[0m"
COLOR_SEQ = "\033[1;%d;40m"
BOLD_SEQ = "\033[1m"

COLORS = {
    'WARNING': YELLOW,
    'INFO': WHITE,
    'DEBUG': BLUE,
    'CRITICAL': YELLOW,
    'ERROR': RED
}

class ColoredFormatter(logging.Formatter):
    def __init__(self, msg, use_color = True):
        logging.Formatter.__init__(self, msg)
        self.use_color = use_color

    def format(self, record):
        levelname = record.levelname
        color     = COLOR_SEQ % (30 + COLORS[levelname])
        message   = logging.Formatter.format(self, record)
        message   = message.replace("$RESET", RESET_SEQ)\
                           .replace("$BOLD",  BOLD_SEQ)\
                           .replace("$COLOR", color)
        return message + RESET_SEQ

# ---------------------------------------------------------------------------
# Main routine
# ---------------------------------------------------------------------------
def main():
    global exit_status
    ## logging.basicConfig(level=logging.DEBUG)
    mylog = logging.StreamHandler( )
    logging.getLogger().setLevel( logging.DEBUG )
    mylog.setFormatter( ColoredFormatter( "$COLOR$BOLD[%(levelname)-10s]$RESET$COLOR  %(message)s" , True ) )
    logging.getLogger().addHandler( mylog )
    usage = "usage: %prog [options]"
    parser = OptionParser( usage = usage , version = version )
    parser.add_option( "-q" , "--quiet" , dest="verbose" , default = False ,
                      action = "store_false" ,
                      help = "switch off info printout" )
    parser.add_option( "--remove" , dest="remove" , default = False ,
                      action = "store_true" ,
                      help = "force the delete of the option file before "
                             + "creating a new one, by default existing option "
                             + "files are not overwritten" )
    parser.add_option( "-d" , "--decay" , type = "string" , dest = "NickName" ,
                      help = "name of the nick name of the decay to create option "
                      + "for, if not specified, loop over all decay files in the "
                      + "dkfiles directory" ,
                      action = "callback" , callback = CheckFile )
    parser.add_option( "--text" , dest = "python" , default = True ,
                      action = "store_false" ,
                      help = "create text option files instead of python options" )
    parser.add_option( "--force" , dest = "force" , default = False ,
                      action = "store_true" ,
                      help = "force create of option file even when the decay file " +
                      "syntax is not correct" )

    ## Check that the environment variable DECFILESROOT exist otherwise
    ## set it to ../dkfiles
    if "DECFILESROOT" not in os.environ:
        logging.warning( "" )
        logging.warning( "The variable DECFILESROOT is not defined." )
        logging.warning( "Use ../ instead." )
        logging.warning( "Run the setup script of the package to set the correct value." )
        logging.warning( "" )
        os.environ["DECFILESROOT"]="../"
    else:
        logging.info( "" )
        logging.info( "The DECFILESROOT environment variable is set to: %s" , os.environ['DECFILESROOT'] )
        logging.info( "" )

    (options, args) = parser.parse_args()

    if not options.verbose:
        logging.getLogger().setLevel( logging.WARNING )

    readObsoleteTypeTable()

    if options.NickName:
        try:
            run_create( '{0}/dkfiles/{1}.dec'.format( os.environ[ 'DECFILESROOT' ] , options.NickName ) , options.remove , options.python , options.force )
        except UserWarning:
            exit_status = 1
            pass
    else:
        run_loop( options.remove , options.python , options.force )

if __name__ == "__main__":
    main()
    sys.exit( exit_status )
