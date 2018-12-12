"""
Module for construction of B->KShh stripping Selections and StrippingLines.
Provides functions to build KS->DD, KS->LL, KS->LD and B selections.
Provides class B2KShhConf, which constructs the Selections and StrippingLines
given a configuration dictionary.
Selections based on previous version B2KShh line but optimised for DP analysis.
Exported symbols (use python help!):
   - B2KShhConf
   - default_config
"""

__author__ = ['Thomas Latham','Rafael Coutinho']
__date__ = '01/04/2016'
__version__ = 'Stripping26'
__all__ = {'B2KShhConf',
           'default_config'}

from Gaudi.Configuration import *
from GaudiConfUtils.ConfigurableGenerators import FilterDesktop, DaVinci__N3BodyDecays
from PhysSelPython.Wrappers import Selection, DataOnDemand
from StrippingConf.StrippingLine import StrippingLine
from StrippingUtils.Utils import LineBuilder

from StandardParticles import StdAllNoPIDsPions as Pions

default_config = {
    'NAME'        : 'B2KShh',
    'WGs'         : ['BnoC'],
    'BUILDERTYPE' : 'B2KShhConf',
    'CONFIG'      : {'Trk_Chi2'                : 4.0,
                     'Trk_GhostProb'           : 0.5,
                     'KS_DD_MassWindow'        : 30.0,
                     'KS_DD_VtxChi2'           : 12.0,
                     'KS_DD_FDChi2'            : 50.0,
                     'KS_DD_Pmin'              : 6000.0,
                     'KS_LD_MassWindow'        : 25.0,
                     'KS_LD_VtxChi2'           : 12.0,
                     'KS_LD_FDChi2'            : 50.0,
                     'KS_LD_Pmin'              : 6000.0,
                     'KS_LL_MassWindow'        : 20.0,
                     'KS_LL_VtxChi2'           : 12.0,
                     'KS_LL_FDChi2'            : 80.0,
                     'KS_LL_Pmin'              : 0.0,
                     'B_Mlow'                  : 1279.0,
                     'B_Mhigh'                 : 921.0,
                     'B_APTmin'                : 1000.0,
                     'BDaug_MedPT_PT'          : 800.0,
                     'BDaug_MaxDOCAChi2'       : 25.0,
                     'BDaug_DD_PTsum'          : 4200.0,
                     'BDaug_LD_PTsum'          : 4200.0,
                     'BDaug_LL_PTsum'          : 3000.0,
                     'B_PTmin'                 : 1500.0,
                     'B_VtxChi2'               : 12.0,
                     'KS_FD_Z'                 : 15.,
                     'B_DD_Dira'               : 0.999,
                     'B_LD_Dira'               : 0.999,
                     'B_LL_Dira'               : 0.999,
                     'B_DD_IPChi2'             : 6.0,
                     'B_LD_IPChi2'             : 7.0,
                     'B_LL_IPChi2'             : 8.0,
                     'B_DD_FDChi2'             : 50.0,
                     'B_LD_FDChi2'             : 50.0,
                     'B_LL_FDChi2'             : 50.0,
                     'BDaug_DD_IPChi2sum'      : 50.0,
                     'BDaug_LD_IPChi2sum'      : 50.0,
                     'BDaug_LL_IPChi2sum'      : 50.0,
                     'GEC_MaxTracks'           : 250,
                     'ConeAngles'              : [ 1.0, 1.5, 1.7, 2.0 ],
                     # Run1 Triggers
                     #'HLT1Dec'                 : 'Hlt1TrackAllL0Decision',
                     #'HLT2Dec'                 : 'Hlt2Topo[234]Body.*Decision',
                     # Run2 Triggers
                     'HLT1Dec'                 : 'Hlt1(Two)?TrackMVADecision|Hlt1IncPhiDecision',
                     'HLT2Dec'                 : 'Hlt2Topo[234]BodyDecision|Hlt2IncPhiDecision',
                     'FlavourTagging'          : False,
                     'MDST'                    : False,
                     'Prescale'                : 1.0,
                     'Prescale_SameSign'       : 1.0,
                     'Postscale'               : 1.0
                     },
    'STREAMS'     : {
                     'BhadronCompleteEvent' : [
                         'StrippingB2KShh_DD_2016_OS_Line',
                         'StrippingB2KShh_LL_2016_OS_Line',
                         'StrippingB2KShh_LD_2016_OS_Line',
                         ] ,
                     'Bhadron' : [
                         'StrippingB2KShh_DD_2016_SS_Line',
                         'StrippingB2KShh_LL_2016_SS_Line',
                         'StrippingB2KShh_LD_2016_SS_Line',
                         ]
                     }
    }

class B2KShhConf(LineBuilder) :
    """
    Builder of B->KShh stripping Selection and StrippingLine.
    Constructs B -> KS h+ h- Selections and StrippingLines from a configuration dictionary.
    Usage:
    >>> config = { .... }
    >>> b2kshhConf  = B2KShhConf('B2KShhTest',config)
    >>> b2kshhLines = b2kshhConf.lines
    >>> for line in line :
    >>>  print line.name(), line.outputLocation()
    The lines can be used directly to build a StrippingStream object.

    Exports as instance data members:
    selKS2DD               : KS -> Down Down Selection object
    selKS2LL               : KS -> Long Long Selection object
    selKS2LD               : KS -> Long Down Selection object
    selB2KSDDhh            : B -> KS(DD) h+ h- Selection object
    selB2KSLLhh            : B -> KS(LL) h+ h- Selection object
    selB2KSLDhh            : B -> KS(LD) h+ h- Selection object
    selB2KSDDhh_SameSign   : B -> KS(DD) h+(-) h+(-) Selection object
    selB2KSLLhh_SameSign   : B -> KS(LL) h+(-) h+(-) Selection object
    selB2KSLDhh_SameSign   : B -> KS(LD) h+(-) h+(-) Selection object
    dd_line                : StrippingLine made out of selB2KSDDhh
    ll_line                : StrippingLine made out of selB2KSLLhh
    ld_line                : StrippingLine made out of selB2KSLDhh
    dd_line_same           : StrippingLine made out of selB2KSDDhh_SameSign
    ll_line_same           : StrippingLine made out of selB2KSLLhh_SameSign
    ld_line_same           : StrippingLine made out of selB2KSLDhh_SameSign
    lines                  : List of lines, [dd_line, ll_line, ld_line, dd_line_same, ll_line_same, ld_line_same]

    Exports as class data member:
    B2KShhConf.__configuration_keys__ : List of required configuration parameters.
    """

    __configuration_keys__ = ('Trk_Chi2',
                              'Trk_GhostProb',
                              'KS_DD_MassWindow',
                              'KS_DD_VtxChi2',
                              'KS_DD_FDChi2',
                              'KS_DD_Pmin',
                              'KS_LD_MassWindow',
                              'KS_LD_VtxChi2',
                              'KS_LD_FDChi2',
                              'KS_LD_Pmin',
                              'KS_LL_MassWindow',
                              'KS_LL_VtxChi2',
                              'KS_LL_FDChi2',
                              'KS_LL_Pmin',
                              'B_Mlow',
                              'B_Mhigh',
                              'B_APTmin',
                              'BDaug_MedPT_PT',
                              'BDaug_MaxDOCAChi2',
                              'BDaug_DD_PTsum',
                              'BDaug_LD_PTsum',
                              'BDaug_LL_PTsum',
                              'B_PTmin',
                              'B_VtxChi2',
                              'KS_FD_Z',
                              'B_DD_Dira',
                              'B_LD_Dira',
                              'B_LL_Dira',
                              'B_DD_IPChi2',  
                              'B_LD_IPChi2', 
                              'B_LL_IPChi2',
                              'B_DD_FDChi2',  
                              'B_LD_FDChi2', 
                              'B_LL_FDChi2',
                              'BDaug_DD_IPChi2sum',  
                              'BDaug_LD_IPChi2sum', 
                              'BDaug_LL_IPChi2sum',
                              'GEC_MaxTracks',
                              'ConeAngles',
                              'HLT1Dec',
                              'HLT2Dec',
                              'FlavourTagging',
                              'MDST',
                              'Prescale',
                              'Prescale_SameSign',
                              'Postscale'
                              )

    def __init__(self, name, config) :

        LineBuilder.__init__(self, name, config)

        _ks_types = [ 'DD', 'LL', 'LD' ]
        _years = [ '2016' ]
        _signs = [ 'OS', 'SS' ]

        GECFilter = {'Code' : "(recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) < %s)" % config['GEC_MaxTracks'],
                   'Preambulo' : ["from LoKiTracks.decorators import *"]}

        Hlt1Filter = {'Code' : "HLT_PASS_RE('%s')" % config['HLT1Dec'],
                     'Preambulo' : ["from LoKiCore.functions import *"]}
                          
        Hlt2Filter = {'Code' : "HLT_PASS_RE('%s')" % config['HLT2Dec'],
                     'Preambulo' : ["from LoKiCore.functions import *"]}

        # the related info tools
        relinfo = [ self.getRelInfoConeTool( angle ) for angle in config['ConeAngles'] ]
        relinfo.append( self.getRelInfoVtxIsoTool() )

        # the input charged particles
        self.pions = Pions

        # build the various KS input lists
        self.selKS = {}
        for ks_type in _ks_types :
            self.selKS[ks_type] = self.makeKS( 'KSfor'+name+ks_type, ks_type, config )

        # build the various B's
        _selB = {}
        _mylines = {}
        for ks_type in _ks_types :
            _selB[ks_type] = {}
            _mylines[ks_type] = {}

            for year in _years :
                _selB[ks_type][year] = {}
                _mylines[ks_type][year] = {}

                for sign in _signs :

                    _linename = name+'_'+ks_type+'_'+year+'_'+sign+'_Line'

                    _selB[ks_type][year][sign] = self.makeB2KShh( name, ks_type, year, sign, config )

                    # Main Algorithm initialisation
                    _flavourFlag = config['FlavourTagging']
                    if sign == 'SS' : 
                        _flavourFlag = False

                    _mylines[ks_type][year][sign] = StrippingLine(_linename,
                                           prescale = config['Prescale'],
                                           postscale = config['Postscale'],
                                           selection = _selB[ks_type][year][sign],
                                           HLT1 = Hlt1Filter,
                                           HLT2 = Hlt2Filter,
                                           FILTER = GECFilter,
                                           RelatedInfoTools = relinfo, 
                                           EnableFlavourTagging = _flavourFlag,
                                           MDSTFlag = config['MDST']
                                           )
        

                    self.registerLine(_mylines[ks_type][year][sign])


    def makeKS( self, name, ks_type, config ) :
        # define all the cuts
        _massCut          = "(ADMASS('KS0')<%s*MeV)"         % config['KS_%s_MassWindow'%ks_type]
        _vtxCut           = "(VFASPF(VCHI2)<%s)"             % config['KS_%s_VtxChi2'%ks_type]
        _fdCut            = "(BPVVDCHI2>%s)"                 % config['KS_%s_FDChi2'%ks_type]
        _momCut           = "(P>%s*MeV)"                     % config['KS_%s_Pmin'%ks_type]
        _trkChi2Cut1      = "(CHILDCUT((TRCHI2DOF<%s),1))"   % config['Trk_Chi2']
        _trkChi2Cut2      = "(CHILDCUT((TRCHI2DOF<%s),2))"   % config['Trk_Chi2']
        _trkGhostProbCut1 = "(CHILDCUT((TRGHOSTPROB<%s),1))" % config['Trk_GhostProb']
        _trkGhostProbCut2 = "(CHILDCUT((TRGHOSTPROB<%s),2))" % config['Trk_GhostProb']

        _allCuts = _trkChi2Cut1
        _allCuts += '&'+_trkChi2Cut2

        if ks_type == 'LL' :
            _allCuts += '&'+_trkGhostProbCut1
            _allCuts += '&'+_trkGhostProbCut2
        else :
            _allCuts += '&'+_momCut

        _allCuts += '&'+_massCut
        _allCuts += '&'+_vtxCut
        _allCuts += '&'+_fdCut

        # get the KS's to filter
        _stdKS = DataOnDemand( Location = 'Phys/StdLooseKs%s/Particles' % ks_type )

        # make the filter
        _filterKS = FilterDesktop( Code = _allCuts )

        # make and return the Selection object
        return Selection( name, Algorithm = _filterKS, RequiredSelections = [_stdKS] )


    def makeB2KShh( self, name, ks_type, year, sign, config ) :
        """
        Create and return either a B -> KS h+ h- Selection object, or a B -> KS h+(-) h+(-) Same Sign Selection Object
        Arguments:
        name             : name of the Selection.
        ks_type          : type of the KS, e.g. DD
        year             : the year for which we are making the selection
        sign             : whether we use opposite-sign or same-sign h's
        config           : config dictionary
        """

        _trkChi2Cut      = "(TRCHI2DOF<%s)"   % config['Trk_Chi2']
        _trkGhostProbCut = "(TRGHOSTPROB<%s)" % config['Trk_GhostProb']

        _daughtersCuts = _trkChi2Cut+'&'+_trkGhostProbCut

        _massCutLow       = "(AM>(5279-%s)*MeV)"        % config['B_Mlow']
        _massCutHigh      = "(AM<(5279+%s)*MeV)"        % config['B_Mhigh']
        _aptCut           = "(APT>%s*MeV)"              % config['B_APTmin']
        _daugPtSumCut     = "((APT1+APT2+APT3)>%s*MeV)" % config['BDaug_%s_PTsum' % ks_type]
        _daugMedPtCut     = "(ANUM(PT>%s*MeV)>=2)"      % config['BDaug_MedPT_PT']
        _maxDoca12Chi2Cut = "(ACHI2DOCA(1,2)<%s)"       % config['BDaug_MaxDOCAChi2']
        _maxDoca13Chi2Cut = "(ACHI2DOCA(1,3)<%s)"       % config['BDaug_MaxDOCAChi2']
        _maxDoca23Chi2Cut = "(ACHI2DOCA(2,3)<%s)"       % config['BDaug_MaxDOCAChi2']

        _comb12Cuts = _massCutHigh+'&'+_maxDoca12Chi2Cut
        _combCuts = _daugPtSumCut+'&'+_massCutLow+'&'+_massCutHigh+'&'+_aptCut+'&'+_daugMedPtCut+'&'+_maxDoca13Chi2Cut+'&'+_maxDoca23Chi2Cut

        _ptCut            = "(PT>%s*MeV)"                                    % config['B_PTmin']
        _vtxChi2Cut       = "(VFASPF(VCHI2)<%s)"                             % config['B_VtxChi2']
        _KSdiffZ          = "((CHILD(VFASPF(VZ),3) - VFASPF(VZ))>%s*mm)"     % config['KS_FD_Z']
        _diraCut          = "(BPVDIRA>%s)"                                   % config['B_%s_Dira' % ks_type]
        _ipChi2Cut        = "(BPVIPCHI2()<%s)"                               % config['B_%s_IPChi2' % ks_type]
        _fdChi2Cut        = "(BPVVDCHI2>%s)"                                 % config['B_%s_FDChi2' % ks_type]
        _ipChi2SumCut     = "(SUMTREE(BPVIPCHI2(),(ABSID=='pi+'),0.0) > %s)" % config['BDaug_%s_IPChi2sum' % ks_type]

        _motherCuts = _ptCut+'&'+_vtxChi2Cut+'&'+_KSdiffZ+'&'+_diraCut+'&'+_ipChi2Cut+'&'+_fdChi2Cut+'&'+_ipChi2SumCut

        _B = DaVinci__N3BodyDecays()

        if sign == 'OS' :
            _B.DecayDescriptors = [ "B0 -> pi+ pi- KS0" ]
        else:
            _B.DecayDescriptors = [ "B0 -> pi+ pi+ KS0", "B0 -> pi- pi- KS0" ]

        _B.DaughtersCuts    = { "pi+" : _daughtersCuts }
        _B.Combination12Cut = _comb12Cuts
        _B.CombinationCut   = _combCuts
        _B.MotherCut        = _motherCuts
        _B.ReFitPVs         = True 

        _selname = name + '_' + ks_type + '_' + year + '_' + sign + '_Presel'

        return Selection (_selname, Algorithm = _B, RequiredSelections = [ self.selKS[ks_type], self.pions ])


    @staticmethod
    def getRelInfoConeTool( angle ) :
        """
        Create a RelInfoConeVariables dictionary for the given angle
        """
        angle_str = str(angle)
        angle_str = angle_str.replace('.','')
        tool = {
                  "Type"              : "RelInfoConeVariables"
                , "ConeAngle"         : angle
                , "Variables"         : ['CONEANGLE', 'CONEMULT', 'CONEPXASYM', 'CONEPYASYM', 'CONEPZASYM', 'CONEPASYM', 'CONEPTASYM', 'CONEDELTAETA', 'CONEDELTAPHI']
                , 'Location'          : 'ConeVar%s_B' % angle_str
                , "DaughterLocations" : { "B0 -> Meson Meson ^KS0" : 'ConeVar%s_KS' % angle_str }
               }
        return tool


    @staticmethod
    def getRelInfoVtxIsoTool() :
        """
        Create a RelInfoVertexIsolation dictionary
        """
        tool = {
                  "Type"              : "RelInfoVertexIsolation"
                , "Variables"         : ['VTXISONUMVTX', 'VTXISODCHI2ONETRACK', 'VTXISODCHI2MASSONETRACK', 'VTXISODCHI2TWOTRACK', 'VTXISODCHI2MASSTWOTRACK']
                , 'Location'          : 'VtxIsolationVar_B'
                , "DaughterLocations" : { "B0 -> Meson Meson ^KS0" : 'VtxIsolationVar_KS' }
               }
        return tool


