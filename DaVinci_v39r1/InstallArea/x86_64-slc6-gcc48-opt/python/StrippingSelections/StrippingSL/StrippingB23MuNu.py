
__author__ = 'P. Owen'
__date__ = '26/06/20114'
__version__ = '$Revision: 1.0 $'

__all__ = ( 'B23MuNuConf' )

"""
Stripping selection for B to three muons and a neutrino.
"""

from Gaudi.Configuration import *
from GaudiConfUtils.ConfigurableGenerators import  CombineParticles, FilterDesktop

from PhysSelPython.Wrappers import Selection, AutomaticData, MergedSelection
from StrippingConf.StrippingLine import StrippingLine
from StrippingUtils.Utils import LineBuilder
from LHCbKernel.Configuration import *  #check if needed
from Configurables import SubstitutePID
from Configurables import SubPIDMMFilter


#################
#
#  Define Cuts here
#
#################

default_config = {
    'B23MuNu' : {
        'WGs'         : ['Semileptonic'],
	'BUILDERTYPE' : 'B23MuNuConf',
        'CONFIG'      : {
	  #  (dimu) cuts
	  'FlightChi2'      :    50.0,
	  'DIRA'            :   0.999,
	  'BPT'             :  2000.0,
	  'VertexCHI2'      :     4.0,
	  'LOWERMASS'       :     0.0, # MeV
	  'UPPERMASS'       :  7500.0, # MeV
	  'CORRM_MIN'       :  2500.0, # MeV
	  'CORRM_MAX'       : 10000.0, # MeV
	  # Track cuts
	  'Track_CHI2nDOF'      :    3.0,
	  'Track_GhostProb'     :    0.35,  

	  # Muon cuts
	  'Muon_MinIPCHI2'   :    9.0,
	  'Muon_PIDmu'       :    0.0,
	  'Muon_PIDmuK'      :    0.0,
	  'Muon_PT'          :    0,

	  # GEC
	  'SpdMult'             :  600,

    'MisIDPrescale'       : 0.01,
	 },
       'STREAMS'     : ['Semileptonic']	  
      }
    }

defaultName = "B23MuNu"


class B23MuNuConf(LineBuilder) :

    __configuration_keys__ = (
       #  (dimu) cuts
        'FlightChi2',
        'VertexCHI2',
        'DIRA',
        'BPT',
        'LOWERMASS',
        'UPPERMASS',
        'CORRM_MIN',
        'CORRM_MAX',

        # Track cuts
        'Track_CHI2nDOF',
        'Track_GhostProb',
        
        # Muon cuts
        'Muon_MinIPCHI2',
        'Muon_PIDmu',
        'Muon_PIDmuK',
        'Muon_PT',


        #GEC
        'SpdMult',

        'MisIDPrescale',

        )
    
    def __init__(self, name, config) :


        LineBuilder.__init__(self, name, config)

        self.name = name
        

        self.TriMuCut = "(BPVCORRM > %(CORRM_MIN)s *MeV) & " \
                           "(BPVCORRM < %(CORRM_MAX)s *MeV) & " \
                                "(BPVDIRA > %(DIRA)s) & " \
                                "(PT > %(BPT)s) & " \
                                "(BPVVDCHI2 > %(FlightChi2)s) & " \
                                "(VFASPF(VCHI2/VDOF) < %(VertexCHI2)s) & " \
                                "(M > %(LOWERMASS)s) & " \
                                "(M < %(UPPERMASS)s) " %config

        self.TrackCuts = "(TRCHI2DOF < %(Track_CHI2nDOF)s) & (TRGHP < %(Track_GhostProb)s)" \
                         " & (MIPCHI2DV(PRIMARY) > %(Muon_MinIPCHI2)s) " \
                         " & (PT > %(Muon_PT)s)" %config
        
        self.MuonCut = self.TrackCuts + "& (PIDmu> %(Muon_PIDmu)s) & " \
                                        " (PIDmu-PIDK> %(Muon_PIDmuK)s)" %config

        self.Muons = self.__Muons__(config)
        self.FakeMuons = self.__FakeMuons__(config)
        self.Jpsi = self.__Jpsi__(config)
        self.Trimu = self.__Trimu__(config)
        self.FakeTrimu = self.__FakeTrimu__(config)

        


        # inclusive dimuon line
        self.TriMu_line =  StrippingLine(
            self.name+"_TriMuLine",
            prescale = 1,
            FILTER = {
            'Code' : " ( recSummary(LHCb.RecSummary.nSPDhits,'Raw/Spd/Digits') < %(SpdMult)s )" %config ,
            'Preambulo' : [
            "from LoKiNumbers.decorators import *", "from LoKiCore.basic import LHCb"
            ]
            },
            algos=[self.Trimu]
            )

        self.FakeTriMu_line =  StrippingLine(
            self.name+"_TriFakeMuLine",
            prescale = config['MisIDPrescale'],
            FILTER = {
            'Code' : " ( recSummary(LHCb.RecSummary.nSPDhits,'Raw/Spd/Digits') < %(SpdMult)s )" %config ,
            'Preambulo' : [
            "from LoKiNumbers.decorators import *", "from LoKiCore.basic import LHCb"
            ]
            },
            algos=[self.FakeTrimu]
            )

        self.registerLine( self.TriMu_line )
        self.registerLine( self.FakeTriMu_line )

        # inclusive dimuon line around jpsi and psi2s


    def __Muons__(self, conf):
        """
        Filter muons from StdLooseMuons
        """  
        from StandardParticles import StdAllLooseMuons
        _muons = StdAllLooseMuons
        _filter = FilterDesktop(Code = self.MuonCut)
        _sel = Selection("Selection_"+self.name+"_Muons",
                         RequiredSelections = [ _muons ] ,
                         Algorithm = _filter)
        return _sel
 
        
    def __FakeMuons__(self, conf):
        """
        Filter muons from StdLooseMuons
        """  
        from StandardParticles import StdAllNoPIDsMuons
        _fakemuons = StdAllNoPIDsMuons
        _filter = FilterDesktop(Code = self.TrackCuts)
        _sel = Selection("Selection_"+self.name+"_FakeMuons",
                         RequiredSelections = [ _fakemuons ] ,
                         Algorithm = _filter)
        return _sel

    def __Jpsi__(self, conf):
        """
        Creates Jpsi as proxy for dimuon
        """
        from PhysSelPython.Wrappers import AutomaticData, Selection, SelectionSequence, DataOnDemand, MergedSelection
        from  GaudiConfUtils.ConfigurableGenerators import CombineParticles
        #from Configurables import CombineParticles 

        CombineJpsi= CombineParticles(DecayDescriptors = ["J/psi(1S) -> mu+ mu-","[J/psi(1S) -> mu+ mu+]cc"],       			    
       			     MotherCut = "ALL")
        
        sel_name = "Jpsi"
        
        from PhysSelPython.Wrappers import Selection
        SelJpsi = Selection("Sel_" + self.name + "_Jpsi", Algorithm = CombineJpsi,
                              RequiredSelections = [ self.Muons ] )
        return SelJpsi

    def __Trimu__(self, conf):
        '''
        Create trimuon
        '''
        from  GaudiConfUtils.ConfigurableGenerators import CombineParticles
        CombineTriMuon = CombineParticles()
        CombineTriMuon.DecayDescriptors = ["[B+ -> mu+ mu+ mu-]cc", "[B+ -> mu+ mu+ mu+]cc"]
        sel_name="TriMu"
        CombineTriMuon.MotherCut     = self.TriMuCut
        # choose

        from PhysSelPython.Wrappers import Selection
        SelTriMuon = Selection("Sel_" + self.name + "_"+sel_name, 
                              Algorithm = CombineTriMuon,
                              RequiredSelections = [ self.Muons ] )
        return SelTriMuon
   

    def __FakeTrimu__(self, conf):
        """
        Create trimuon
        """

        CombineTriMuon = CombineParticles()
        CombineTriMuon.DecayDescriptor = "[B+ -> J/psi(1S) mu+]cc"
        sel_name="FakeTriMu"
        #CombineTriMuon.CombinationCut = self.TriMuLowQ2CombCut
        #["[B+ ->mu+ mu+ mu-]cc", "[B+ ->mu+ mu+ mu+]cc"]
        CombineTriMuon.MotherCut     = self.TriMuCut
        # choose

        from PhysSelPython.Wrappers import Selection
        #SelTriMuon = Selection("Sel_" + self.name + "_"+sel_name, Algorithm = CombineTriMuon,
        #                      RequiredSelections = [self.Jpsi, self.FakeMuon ])
        SelTriMuon = Selection(sel_name,
                 Algorithm = CombineTriMuon,
                 RequiredSelections = [ self.FakeMuons, self.Jpsi ])


        return SelTriMuon
 
