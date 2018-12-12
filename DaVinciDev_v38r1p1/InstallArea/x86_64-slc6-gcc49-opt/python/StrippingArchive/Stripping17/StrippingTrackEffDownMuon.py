## #####################################################################
# A stripping selection for Downstream J/psi->mu+mu- decays
# To be used for tracking studies
#
# @authors G. Krocker, P. Seyfert, S. Wandernoth
# @date 2010-Aug-17
#
# @authors P. Seyfert, A. Jaeger
# @date 2011-Mar-17
# 
#######################################################################

#FIXME Write includes in a cleaner way
from Gaudi.Configuration import *
from LHCbKernel.Configuration import *
from Configurables import GaudiSequencer 
from Configurables import UnpackTrack, ChargedProtoParticleMaker, DelegatingTrackSelector, TrackSelector, BestPIDParticleMaker
from TrackFitter.ConfiguredFitters import ConfiguredFit
from Configurables import TrackStateInitAlg
from StrippingConf.StrippingLine import StrippingLine
from Configurables import ChargedProtoParticleAddMuonInfo, MuonIDAlg
from MuonID import ConfiguredMuonIDs
from Configurables import ChargedProtoCombineDLLsAlg, ProtoParticleMUONFilter 
from PhysSelPython.Wrappers import Selection, DataOnDemand
from GaudiConfUtils.ConfigurableGenerators import FilterDesktop, CombineParticles

from StrippingUtils.Utils import LineBuilder
from Configurables import LoKi__VoidFilter
from os import environ
from Gaudi.Configuration import *
import GaudiKernel.ProcessJobOptions
from GaudiKernel.SystemOfUnits import mm

from GaudiConfUtils.ConfigurableGenerators import TisTosParticleTagger
from StandardParticles import StdAllLooseMuons
#from StandardParticles import StdLooseMuons
from Configurables import GaudiSequencer
from Configurables import TrackToDST
from Configurables import TrackSys
from Configurables import PatSeeding, PatDownstream
from PhysSelPython.Wrappers import AutomaticData
# Get the fitters
from TrackFitter.ConfiguredFitters import ConfiguredFit, ConfiguredFitSeed, ConfiguredFitDownstream
from PatAlgorithms import PatAlgConf

from SelPy.utils import ( UniquelyNamedObject,
                          ClonableObject,
                          SelectionBase )

#name = "TrackEffDownMuonLine"

confdict={
			'MuMom':		2000.	# MeV
		,	'MuTMom':		200.	# MeV
		,	'TrChi2':		10.	# MeV
		,	'MassPreComb':		2000.	# MeV
		,	'MassPostComb':		200.	# MeV
		,	'Doca':			5.	# mm
		,	'VertChi2':		25.	# adimensional
                ,       'DataType':             '2011'        
		,	'NominalLinePrescale':  0.2 # proposal: 0.2 to stay below 0.15% retention rate 
		,	'NominalLinePostscale': 1.
		,	'ValidationLinePrescale':0.003 #0.5 in stripping15: 0.1 gives 1.42% retention rate
		,	'ValidationLinePostscale': 1.
		,	'HLT1TisTosSpecs': { "Hlt1TrackMuonDecision%TOS" : 0, "Hlt1SingleMuonNoIPL0Decision%TOS" : 0} #no reg. expression allowed(see selHlt1Jpsi )
		,	'HLT1PassOnAll': True
		,	'HLT2TisTosSpecs': { "Hlt2SingleMuon.*Decision%TOS" : 0} #reg. expression allowed
		,	'HLT2PassOnAll': False

    }

class StrippingTrackEffDownMuonConf(LineBuilder):
    """
    Definition of Downstream J/Psi stripping.
    """
    
    __configuration_keys__ = (
		    		'MuMom',
				'MuTMom',
				'TrChi2',
				'MassPreComb',
				'MassPostComb',
				'Doca',
				'VertChi2',
				'DataType',
                              	'NominalLinePrescale',
                              	'NominalLinePostscale',
                              	'ValidationLinePrescale',
                              	'ValidationLinePostscale',
				'HLT1TisTosSpecs',
		   	        'HLT1PassOnAll',
				'HLT2TisTosSpecs',
				'HLT2PassOnAll'
                              )
				

    def __init__(self, name, config) :

        LineBuilder.__init__(self, name, config)
	
	nominal_name = name + 'Nominal'
	valid_name = name + 'Validation'
        
	self.TisTosPreFilter1Jpsi = selHlt1Jpsi('TisTosFilter1Jpsi'+name, HLT1TisTosSpecs = config['HLT1TisTosSpecs'], HLT1PassOnAll = config['HLT1PassOnAll'])
	self.TisTosPreFilter2Jpsi = selHlt2Jpsi('TisTosFilter2Jpsi'+name, hlt1Filter = self.TisTosPreFilter1Jpsi, HLT2TisTosSpecs = config['HLT2TisTosSpecs'], HLT2PassOnAll = config['HLT2PassOnAll'])

	self.TrackingPreFilter = trackingDownPreFilter('TrackingPreFilter' + nominal_name, self.TisTosPreFilter2Jpsi)
	self.DownMuProtoPFilter = selMuonPParts('DownMuon'+nominal_name, config['DataType'], self.TrackingPreFilter)
	self.DownMuPFilter = makeMyMuons('DownMuon'+nominal_name, self.DownMuProtoPFilter)
	self.DownJpsiFilter = DownJPsi( 'DownJpsiSel'+nominal_name, self.DownMuPFilter, config['TrChi2'], 
			config['MuTMom'], config['MuMom'], config['MassPreComb'], config['Doca'], 
			config['MassPostComb'], config['VertChi2'] )

	self.nominal_line =  StrippingLine(nominal_name + 'Line',  prescale = config['NominalLinePrescale'], postscale = config['NominalLinePostscale'], algos=[self.DownJpsiFilter])

	self.valid_line = StrippingLine(valid_name + 'Line', prescale = config['ValidationLinePrescale'], postscale = config['ValidationLinePostscale'], algos=[self.TisTosPreFilter2Jpsi])
        
	self.registerLine(self.nominal_line)
        self.registerLine(self.valid_line)

# ########################################################################################
# Make the protoparticles
# ########################################################################################
def selMuonPParts(name, DataType, downstreamSeq):
   """
       Make ProtoParticles out of Downstream tracks
   """
   unpacker = UnpackTrack(name+"UnpackTrack")  # do we need this or is it here for historical reason ?
   unpacker.InputName="pRec/Downstream/FittedTracks"
   unpacker.OutputName="Rec/Downstream/FittedTracks"

   idalg = MuonIDAlg(name+"IDalg")
   cm=ConfiguredMuonIDs.ConfiguredMuonIDs( DataType ) #data=DaVinci().getProp("DataType"))
   cm.configureMuonIDAlg(idalg)
   idalg.TrackLocation = "Rec/Downstream/FittedTracks"
   idalg.MuonIDLocation = "Rec/Muon/MuonPID/Downstream"
   idalg.MuonTrackLocation = "Rec/Track/MuonForDownstream" # I would call it FromDownstream

   downprotoseq = GaudiSequencer(name+"ProtoPSeq")
   downprotos = ChargedProtoParticleMaker(name+"ProtoPMaker")
   downprotos.Inputs = ["Rec/Downstream/FittedTracks"]
   downprotos.Output = "Rec/ProtoP/"+name+"ProtoPMaker/ProtoParticles"
   downprotos.addTool( DelegatingTrackSelector, name="TrackSelector" )
   #tracktypes = [ "Long","Upstream","Downstream","Ttrack","Velo","VeloR" ] # only downstream needed 
   tracktypes = ["Downstream"]
   #if (trackcont == "Best") :
   #	tracktypes = [ "Long" ]
   downprotos.TrackSelector.TrackTypes = tracktypes
   selector = downprotos.TrackSelector
   for tsname in tracktypes:
   	selector.addTool(TrackSelector,name=tsname)
   	ts = getattr(selector,tsname)
   	# Set Cuts
   	ts.TrackTypes = [tsname]
#	ts.MinNDoF = 1 
	ts.MaxChi2Cut = 10

   addmuonpid = ChargedProtoParticleAddMuonInfo(name+"addmuoninfo")
   addmuonpid.InputMuonPIDLocation = "Rec/Muon/MuonPID/Downstream"
   addmuonpid.ProtoParticleLocation = "Rec/ProtoP/"+name+"ProtoPMaker/ProtoParticles"
   #addmuonpid.OutputLevel = 0
   combinedll = ChargedProtoCombineDLLsAlg(name+"CombineDLL")
   combinedll.ProtoParticleLocation = "Rec/ProtoP/"+name+"ProtoPMaker/ProtoParticles"
   #combinedll.OutputLevel = 0
   # DST post treatment
   #TrackToDST(name+"TrackToDST").TracksInContainer = "Rec/Downstream/Tracks"
   #downprotoseq.Members += [ TrackToDST(name+"TrackToDST"), downprotos, addmuonpid, combinedll ]
   downprotoseq.Members += [ downprotos, addmuonpid, combinedll ]
#        
   DataOnDemandSvc().AlgMap.update( {
                "/Event/Rec/Downstream/Tracks" : unpacker.getFullName(),
                "/Event/Rec/Muon/MuonPID/Downstream" : idalg.getFullName(),
#                "/Event/Rec/ProtoP/"+name+"ProtoPMaker" : downprotoseq.getFullName()
		} )

   return GSWrapper(name="WrappedDownMuonProtoPSeqFor"+name,
                    sequencer=downprotoseq,
                    output='Rec/ProtoP/' + name +'ProtoPMaker/ProtoParticles',
                    requiredSelections = [ downstreamSeq])
   #     return Selection(name+"_SelPParts", Algorithm = MuonTTPParts, OutputBranch="Rec/ProtoP", Extension="ProtoParticles",RequiredSelections=[downstreamSeq], InputDataSetter=None)

def makeMyMuons(name, protoParticlesMaker):
   """
     Make Particles out of the muon ProtoParticles
   """
   particleMaker =  BestPIDParticleMaker(name+"ParticleMaker" , Particle = "muon")
   particleMaker.addTool(ProtoParticleMUONFilter(Selection = ["RequiresDet='MUON' IsMuonLoose=True"]),name="muon")
   particleMaker.Particles = [ "muon" ]
   particleMaker.Input = "Rec/ProtoP/"+name+"ProtoPMaker/ProtoParticles"
   #particleMaker.OutputLevel = 0

   DataOnDemandSvc().AlgMap.update( {
           "/Event/Phys/" + particleMaker.name() + '/Particles' : particleMaker.getFullName(),
           "/Event/Phys/" + particleMaker.name() + '/Vertices'  : particleMaker.getFullName() 
   } )


   return Selection(name+"SelDownMuonParts", Algorithm = particleMaker, RequiredSelections = [protoParticlesMaker], InputDataSetter=None)

#
def DownJPsi( name,
		protoPartSel,
		TrChi2,
		MuTMom,
		MuMom,
		MassPreComb,
		Doca,
		MassPostComb,
		VertChi2 ) :
   #self.makeMyMuons("DownMuonsForTrackEff", "Downstream")
   
   _MuCuts =  "((TRCHI2DOF < %(TrChi2)s) & (PT > %(MuTMom)s*MeV) & (P > %(MuMom)s*MeV) )" % locals()
   _CombinationCuts = "((ADAMASS('J/psi(1S)') < %(MassPreComb)s * MeV) & (AMAXDOCA('') < %(Doca)s*mm) )" % locals()
   _MotherCuts = "((ADMASS('J/psi(1S)') < %(MassPostComb)s * MeV) & (VFASPF(VCHI2/VDOF) < %(VertChi2)s))" % locals()
   
   _MyDownJpsis = CombineParticles( DecayDescriptor = "J/psi(1S) -> mu+ mu-" ,
   DaughtersCuts = { "mu+": _MuCuts,  "mu-": _MuCuts }, CombinationCut = _CombinationCuts, MotherCut = _MotherCuts)

   return Selection ( name,
                      Algorithm = _MyDownJpsis,
                      RequiredSelections = [protoPartSel])
 
#########################################################################################
"""
Define TisTos Prefilters

"""
#getMuonParticles = DataOnDemand(Location = 'Phys/StdLooseMuons')


#def selHlt1Jpsi(name, longPartsFilter):
def selHlt1Jpsi(name, HLT1TisTosSpecs, HLT1PassOnAll):
   """
   Filter the long track muon to be TOS on a HLT1 single muon trigger,
   for J/psi selection
   """
   #Hlt1Jpsi = TisTosParticleTagger(name+"Hlt1Jpsi")
   Hlt1Jpsi = TisTosParticleTagger(
   TisTosSpecs = HLT1TisTosSpecs #{ "Hlt1TrackMuonDecision%TOS" : 0, "Hlt1SingleMuonNoIPL0Decision%TOS" : 0}
   ,ProjectTracksToCalo = False
   ,CaloClustForCharged = False
   ,CaloClustForNeutral = False
   ,TOSFrac = { 4:0.0, 5:0.0 }
   ,NoRegex = True
   )
   Hlt1Jpsi.PassOnAll = HLT1PassOnAll
   #Hlt1Jpsi.PassOnAll = True # TESTING!
   #
   return Selection(name+"_SelHlt1Jpsi", Algorithm = Hlt1Jpsi, RequiredSelections = [ StdAllLooseMuons ])
   #return Selection(name+"_SelHlt1Jpsi", Algorithm = Hlt1Jpsi, RequiredSelections = [ StdLooseMuons ])

#########################################################
def selHlt2Jpsi(name, hlt1Filter, HLT2TisTosSpecs, HLT2PassOnAll):
   """
   Filter the long track muon to be TOS on a HLT2 single muon trigger,
   for J/psi selection
   """
   #Hlt2Jpsi = TisTosParticleTagger("Hlt2Jpsi")
   Hlt2Jpsi = TisTosParticleTagger(
   TisTosSpecs =HLT2TisTosSpecs #{ "Hlt2SingleMuon.*Decision%TOS" : 0}
   ,ProjectTracksToCalo = False
   ,CaloClustForCharged = False
   ,CaloClustForNeutral = False
   ,TOSFrac = { 4:0.0, 5:0.0 }
   ,NoRegex = False
   )
   Hlt2Jpsi.PassOnAll = HLT2PassOnAll
   #Hlt2Jpsi.PassOnAll = True # TESTING!
   #
   return Selection(name+"_SelHlt2Jpsi", Algorithm = Hlt2Jpsi, RequiredSelections = [ hlt1Filter ])
##########################################################
        

def trackingDownPreFilter(name, prefilter):

    #Jpsi_already_there = LoKi__VoidFilter("Jpsi_already_there")
    #Jpsi_already_there.Code = "1 <= CONTAINS('Rec/Track/Downstream')"

    #Jpsi_not_yet_there = LoKi__VoidFilter("Jpsi_not_yet_there")
    #Jpsi_not_yet_there.Code = "1 > CONTAINS('Rec/Track/Downstream')"

    TrackToDST("DownTrackToDST").TracksInContainer = "Rec/Downstream/FittedTracks"

    #TrackSys().setProp('SpecialData', ['earlyData'])

    jpsidotracking=GaudiSequencer("DownTrackingFor" + name)
    
    #Add seed tracking
    jpsidotracking.Members += [PatSeeding("PatSeeding")]
    PatAlgConf.SeedingConf().configureAlg()
    #Add Seed Fit
    jpsidotracking.Members += [GaudiSequencer("TrackSeedFitSeq")]
    #AddPatDownstream
    downstreamTracking = PatDownstream()
    downstreamTracking.OutputLocation = 'Rec/Downstream/Tracks'
    jpsidotracking.Members += [ downstreamTracking ];
    #AddDownstreamFitSeq
    jpsidotracking.Members += [TrackStateInitAlg("InitSeedDownstream")]
    TrackStateInitAlg("InitSeedDownstream").TrackLocation = "Rec/Downstream/Tracks"
    downstreamFit = ConfiguredFitDownstream()
    downstreamFit.TracksInContainer = 'Rec/Downstream/Tracks'
    downstreamFit.TracksOutContainer = 'Rec/Downstream/FittedTracks'
    jpsidotracking.Members += [downstreamFit]
    jpsidotracking.Members += [TrackToDST("DownTrackToDST")]


    #alg = GaudiSequencer("JpsitracksFor" + name,
    #                     Members = [Jpsi_already_there,
    #                                jpsidotracking],
    #                     ModeOR = True,
    #                     ShortCircuit = True)

    return GSWrapper(name="WrappedDownstreamTracking",
                     sequencer=jpsidotracking,
                     output='Rec/Downstream/FittedTracks',
                     requiredSelections = [ prefilter])



class GSWrapper(UniquelyNamedObject,
                ClonableObject,
                SelectionBase) :
    
    def __init__(self, name, sequencer, output, requiredSelections) :
        UniquelyNamedObject.__init__(self, name)
        ClonableObject.__init__(self, locals())
        SelectionBase.__init__(self,
                               algorithm = sequencer,
                               outputLocation = output,
                               requiredSelections = requiredSelections )



