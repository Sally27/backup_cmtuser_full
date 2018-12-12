
__author__ = 'Paul Schaack'
__date__ = '12/02/2011'
__version__ = '$Revision: 1.0 $'

__all__ = ( 'B2XMuMuConf' )

"""
Stripping selection for B_{s,d} channels
"""

from Gaudi.Configuration import *
from GaudiConfUtils.ConfigurableGenerators import  CombineParticles, FilterDesktop

from PhysSelPython.Wrappers import Selection, AutomaticData, MergedSelection
from StrippingConf.StrippingLine import StrippingLine
from StrippingUtils.Utils import LineBuilder
from LHCbKernel.Configuration import *  #check if needed


#################
#
#  Define Cuts here
#
#################


defaultConfig = {
      'BVXCHI2NDOF'        : 4.0           # dimensionless
    , 'BIPCHI2'            : 9.0           # dimensionless
    , 'BDIRA'              : 0.999968      # dimensionless
    , 'BFDCHI2'            : 100.0         # dimensionless
    , 'KpiMINIPCHI2'       : 9.0           # dimensionless
    , 'KpiTRACKCHI2'       : 4.0           # dimensionless    
    , 'KpiVXCHI2NDOF'      : 9.0           # dimensionless
    , 'MuonMINIPCHI2'      : 16.0           # dimensionless
    , 'MuonTRACKCHI2'      : 4.0           # dimensionless
    , 'MuonPID'            : 0.0           # dimensionless
    , 'DimuonVXCHI2NDOF'   : 9.0           # dimensionless
    , 'DimuonUPPERMASS'    : 5050.0        # MeV
    , 'Pi0MINPT'           : 800.0         # MeV
    , 'DplusLOWERMASS'     : 1600.0        # MeV
    , 'DplusUPPERMASS'     : 2300.0        # MeV      
    , 'KstarplusWINDOW'    : 300.0         # MeV      
}


#################
#
#  Make line here
#
#################

defaultName = "B2XMuMu"


class B2XMuMuConf(LineBuilder) :

    __configuration_keys__ = (
        'BVXCHI2NDOF'
        , 'BIPCHI2'
        , 'BDIRA'
        , 'BFDCHI2'
        , 'KpiMINIPCHI2'
        , 'KpiTRACKCHI2'
        , 'KpiVXCHI2NDOF'
        , 'MuonMINIPCHI2'
        , 'MuonTRACKCHI2'
        , 'MuonPID'
        , 'DimuonVXCHI2NDOF'
        , 'DimuonUPPERMASS'
        , 'Pi0MINPT'
        , 'DplusLOWERMASS'
        , 'DplusUPPERMASS'
        , 'KstarplusWINDOW'
    )

    def __init__(self, name, config) :


        LineBuilder.__init__(self, name, config)

        self.name = name
        self.Muons = self.__Muons__(config)
        self.Dimuon = self.__Dimuon__(self.Muons, config)        
        self.PIDKaons = self.__Kaons__(config)
        self.PIDPions = self.__Pions__(config)
        self.Kaons = self.__NoPIDKaons__(config)
        self.Pions = self.__NoPIDPions__(config)       
        self.Kshort = self.__Kshort__(config)
        self.Pi0 = self.__Pi0__(config)
        self.Phi = self.__Phi__(self.Kaons, config)
        self.Rho = self.__Rho__(self.Pions, config)
        self.Kstar = self.__Kstar__(self.Kaons, self.Pions, config)
        self.Kstar2KsPi = self.__Kstar2KsPi__(self.Kshort, self.Pions, config)
        self.Kstar2KPi0 = self.__Kstar2KPi0__(self.Kaons, self.Pi0, config)

        self.Bs = self.__Bs__(self.Dimuon, self.Kaons, self.Pions,
                              self.Kshort, self.Phi, self.Rho,
                              self.Kstar, self.Kstar2KsPi,
                              self.Kstar2KPi0, config)

        self.line = StrippingLine(self.name+"_Line",
                                  prescale = 1,
                                  algos = [ self.Bs ]
                                  )
        self.registerLine(self.line)



        
    def __DimuonCuts__(self, conf):
        """
        Returns the Dimuon cut string
        """
        _DimuonCuts = """
        (VFASPF(VCHI2/VDOF)< %(DimuonVXCHI2NDOF)s )
        """ % conf
        return _DimuonCuts


    def __MuonCuts__(self, conf):
        """
        Returns the Muon cut string
        """
        _MuonCuts = """
        (PIDmu> %(MuonPID)s ) &
        (TRCHI2DOF < %(MuonTRACKCHI2)s ) &
        (MIPCHI2DV(PRIMARY) > %(MuonMINIPCHI2)s )
        """ % conf
        return _MuonCuts


    def __Muons__(self, conf):
        """
        Filter muons from StdLooseMuons
        """  
        _muons = AutomaticData(Location = 'Phys/StdLooseMuons/Particles')
        _filter = FilterDesktop( Code = self.__MuonCuts__(conf) ) 
        _sel = Selection("Selection_"+self.name+"_Muons",
                         RequiredSelections = [ _muons ] ,
                         Algorithm = _filter)
        return _sel


    def __Dimuon__(self, Muons, conf):
        """
        Make and return a Dimuon
        """      
        _dimuon2mumu = CombineParticles()
        _dimuon2mumu.DecayDescriptors = ["J/psi(1S) -> mu+ mu-", " J/psi(1S) -> mu+ mu+", " J/psi(1S) -> mu- mu-"]
        _dimuon2mumu.CombinationCut = "(AM < %(DimuonUPPERMASS)s *MeV)" % conf
        _dimuon2mumu.MotherCut = self.__DimuonCuts__(conf)
        
        _selDIMUON2MUMU = Selection( "Selection_"+self.name+"_Dimuon",
                                    Algorithm = _dimuon2mumu,
                                    RequiredSelections = [ Muons ] )
        return _selDIMUON2MUMU
    


    def __TrackCuts__(self, conf):
        """
        Returns the KaonPion cut string
        """
        _TrackCuts = """
        (TRCHI2DOF < %(KpiTRACKCHI2)s ) &
        (MIPCHI2DV(PRIMARY) > %(KpiMINIPCHI2)s )
        """ % conf
        return _TrackCuts


    def __Kaons__(self, conf):
        """
        Filter kaons from StdLooseKaons
        """  
        _kaons = AutomaticData(Location = 'Phys/StdLooseKaons/Particles')
        _filter = FilterDesktop(Code = self.__TrackCuts__(conf))
        _sel = Selection("Selection_"+self.name+"_StdLooseKaons",
                         RequiredSelections = [ _kaons ] ,
                         Algorithm = _filter)
        return _sel

    def __NoPIDKaons__(self, conf):
        """
        Filter kaons from StdNoPIDsKaons
        """  
        _kaons = AutomaticData(Location = 'Phys/StdNoPIDsKaons/Particles')
        _filter = FilterDesktop(Code = self.__TrackCuts__(conf))
        _sel = Selection("Selection_"+self.name+"_StdNoPIDsKaons",
                         RequiredSelections = [ _kaons ] ,
                         Algorithm = _filter)
        return _sel



    def __Pions__(self, conf):
        """
        Filter pions from StdLoosePions
        """  
        _pions = AutomaticData(Location = 'Phys/StdLoosePions/Particles')
        _filter = FilterDesktop(Code = self.__TrackCuts__(conf))
        _sel = Selection("Selection_"+self.name+"_StdLoosePions",
                         RequiredSelections = [ _pions ] ,
                         Algorithm = _filter)
        return _sel

    def __NoPIDPions__(self, conf):
        """
        Filter pions from StdNoPIDsPions
        """  
        _pions = AutomaticData(Location = 'Phys/StdNoPIDsPions/Particles')
        _filter = FilterDesktop(Code = self.__TrackCuts__(conf))
        _sel = Selection("Selection_"+self.name+"_StdNoPIDsPions",
                         RequiredSelections = [ _pions ] ,
                         Algorithm = _filter)
        return _sel


    def __KsCuts__(self, conf):
        """
        Returns the KaonPion cut string
        """
        _KsCuts = """
        (MIPCHI2DV(PRIMARY) > %(KpiMINIPCHI2)s )
        """ % conf
        return _KsCuts


    def __Kshort__(self, conf):
        """
        Filter kshort from StdLooseKshort
        """  
        _ksdd = AutomaticData(Location = 'Phys/StdLooseKsDD/Particles')
        _ksll = AutomaticData(Location = 'Phys/StdLooseKsLL/Particles')
        _filter_ksdd = FilterDesktop(Code = self.__KsCuts__(conf))
        _filter_ksll = FilterDesktop(Code = self.__KsCuts__(conf))
        
        _selksdd = Selection("Selection_"+self.name+"_Ksdd",
                             RequiredSelections = [ _ksdd ] ,
                             Algorithm = _filter_ksdd)
        _selksll = Selection("Selection_"+self.name+"_Ksll",
                             RequiredSelections = [ _ksll ] ,
                             Algorithm = _filter_ksll)
        _sel = MergedSelection("Selection_"+self.name+"_Kshort",
                               RequiredSelections = [ _selksdd, _selksll ])
        return _sel



    def __Pi0Cuts__(self, conf):
        """
        Returns the KaonPion cut string
        """
        _Pi0Cuts = """
        (PT > %(Pi0MINPT)s )
        """ % conf
        return _Pi0Cuts



    def __Pi0__(self, conf):
        """
        Filter kshort from Std Pi0
        """  
        _pi0merged = AutomaticData(Location = 'Phys/StdLooseMergedPi0/Particles')
        _pi0resolved = AutomaticData(Location = 'Phys/StdLooseResolvedPi0/Particles')
        _filter_pi0merged = FilterDesktop(Code = self.__Pi0Cuts__(conf))
        _filter_pi0resolved = FilterDesktop(Code = self.__Pi0Cuts__(conf))
        
        _selpi0merged = Selection("Selection_"+self.name+"_Pi0merged",
                                  RequiredSelections = [ _pi0merged ] ,
                                  Algorithm = _filter_pi0merged)
        _selpi0resolved = Selection("Selection_"+self.name+"_pi0resolved",
                                    RequiredSelections = [ _pi0resolved ] ,
                                    Algorithm = _filter_pi0resolved)
        _sel = MergedSelection("Selection_"+self.name+"_Pizero",
                               RequiredSelections = [ _selpi0merged, _selpi0resolved ])
        return _sel



    def __Kstar2KPi0__( self, Kaons, Pi0, conf):
        """
        Make K*(892)+ -> K+ pi0 
        """
        _kstar2kpizero = CombineParticles()
        _kstar2kpizero.DecayDescriptor = "[K*(892)+ -> K+ pi0]cc"
        _kstar2kpizero.MotherCut = "(ADMASS('K*(892)+') < %(KstarplusWINDOW)s *MeV)" % conf

        _kstarConf = _kstar2kpizero.configurable("Combine_"+self.name+"_KPi0")
        _kstarConf.ParticleCombiners.update ( { '' : 'MomentumCombiner' } )
                                                 
        _selKSTAR2KPIZERO = Selection( "Selection_"+self.name+"_Kstar2kpizero",
                                       Algorithm = _kstarConf,
                                       RequiredSelections = [ Kaons, Pi0 ] )
        return _selKSTAR2KPIZERO
        


    def __KpiCuts__(self, conf):
        """
        Returns the Kpi cut string
        """
        _KpiCuts = """
        (VFASPF(VCHI2PDOF)< %(KpiVXCHI2NDOF)s )
        """ % conf
        return _KpiCuts





    def __DplusCuts__(self, conf):
        """
        Returns the Kpi cut string
        """
        _DplusCuts = """
        (M > %(DplusLOWERMASS)s *MeV) &
        (M < %(DplusUPPERMASS)s *MeV)
        """ % conf
        return _DplusCuts


    def __Kstar2KsPi__(self, Kshort, Pions, conf):
        """
        Make a kstarplus
        """      
        _kstar2kspi = CombineParticles()
        _kstar2kspi.DecayDescriptor = "[K*(892)+ -> KS0 pi+]cc"
        _kstar2kspi.MotherCut = self.__KpiCuts__(conf)

        _selKSTAR2KSPI = Selection( "Selection_"+self.name+"_Kstar2kspi",
                                     Algorithm = _kstar2kspi,
                                     RequiredSelections = [ Kshort, Pions ] )
        return _selKSTAR2KSPI



    def __Phi__(self, Kaons, conf):
        """
        Make a phi
        """      
        _phi2kk = CombineParticles()
        _phi2kk.DecayDescriptor = "phi(1020) -> K+ K-"
        _phi2kk.MotherCut = self.__KpiCuts__(conf)

        _selPHI2KK = Selection( "Selection_"+self.name+"_Phi",
                                     Algorithm = _phi2kk,
                                     RequiredSelections = [ Kaons ] )
        return _selPHI2KK
    
    def __Rho__(self, Pions, conf):
        """
        Make a rho
        """      
        _rho2pipi = CombineParticles()
        _rho2pipi.DecayDescriptor = "rho(770)0 -> pi+ pi-"
        _rho2pipi.MotherCut = self.__KpiCuts__(conf)

        _selRHO2PIPI = Selection( "Selection_"+self.name+"_Rho",
                                     Algorithm = _rho2pipi,
                                     RequiredSelections = [ Pions ] )
        return _selRHO2PIPI

    def __Kstar__(self, Kaons, Pions, conf):
        """
        Make a kstar
        """      
        _kstar2kpi = CombineParticles()
        _kstar2kpi.DecayDescriptor = "[K*(892)0 -> K+ pi-]cc"
        _kstar2kpi.MotherCut = self.__KpiCuts__(conf)

        _selKSTAR2KPI = Selection( "Selection_"+self.name+"_Kstar",
                                     Algorithm = _kstar2kpi,
                                     RequiredSelections = [ Kaons, Pions ] )
        return _selKSTAR2KPI

    def __Dplus__(self, Kaons, Pions, conf):
        """
        Make a kstar
        """      
        _dplus2kkp = CombineParticles()
        _dplus2kkp.DecayDescriptors = [
            "D+ -> K+ K- pi+",
            "D- -> K- K+ pi-",
            "D+ -> K+ pi+ pi-",
            "D- -> K- pi- pi+"
            ]
        _dplus2kkp.MotherCut = self.__KpiCuts__(conf) +" & "+ self.__DplusCuts__(conf) 

        _selDPLUS2KKP = Selection( "Selection_"+self.name+"_dplus",
                                     Algorithm = _dplus2kkp,
                                     RequiredSelections = [ Kaons, Pions ] )
        return _selDPLUS2KKP



    def __BsCuts__(self, conf):
        """
        Returns the Bs cut string
        """
        _BsCuts = """
        (VFASPF(VCHI2/VDOF)< %(BVXCHI2NDOF)s ) &
        (BPVVDCHI2 > %(BFDCHI2)s ) &
        (BPVDIRA > %(BDIRA)s ) &
        (BPVIPCHI2()< %(BIPCHI2)s )
        """ % conf
        return _BsCuts






    def __Bs__(self, Dimuon, Kaons, Pions, Kshort, Phi, Rho, Kstar, Kstar2KsPi, Kstar2KPi0, conf):
        """
        Make and return a Bs selection
        """      

        _b2xmumu = CombineParticles()
        _b2xmumu.DecayDescriptors = [ "B0 -> J/psi(1S) phi(1020)",
                                      "[B0 -> J/psi(1S) K*(892)0]cc",
                                      "B0 -> J/psi(1S) rho(770)0",
                                      "B0 -> J/psi(1S) KS0",
                                      "[B+ -> J/psi(1S) K+]cc",
                                      "[B+ -> J/psi(1S) pi+]cc",
                                      "[B+ -> J/psi(1S) K*(892)+]cc"]
        
        _b2xmumu.CombinationCut = "(AM > 5000.0 *MeV) & (AM < 7000.0 *MeV)"
        _b2xmumu.MotherCut = self.__BsCuts__(conf)
        
        _sel_Daughters = MergedSelection("Selection_"+self.name+"_daughters",
                                         RequiredSelections = [Kaons, Pions, Kshort,
                                                               Phi, Rho, Kstar,
                                                               Kstar2KsPi, Kstar2KPi0])
        sel = Selection( "Selection_"+self.name+"_bs2xmumu",
                         Algorithm = _b2xmumu,
                         RequiredSelections = [ Dimuon, _sel_Daughters ])
        return sel





















