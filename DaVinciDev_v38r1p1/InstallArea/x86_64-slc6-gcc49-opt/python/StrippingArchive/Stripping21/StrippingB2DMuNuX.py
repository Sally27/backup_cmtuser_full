__author__ = ['Mika Vesterinen','Liming Zhang, Alessandra Borgia']
__date__ = '23/07/2010'
__version__ = '$Revision: 4.0 $'

from Gaudi.Configuration import *
from GaudiConfUtils.ConfigurableGenerators import FilterDesktop, CombineParticles
from PhysSelPython.Wrappers import Selection, DataOnDemand
from StrippingConf.StrippingLine import StrippingLine
from StrippingUtils.Utils import LineBuilder
from StandardParticles import StdLoosePions, StdLooseMuons, StdLooseKaons, StdLooseProtons, StdNoPIDsPions, StdLooseElectrons

__all__ = ('B2DMuNuXAllLinesConf',
           'makeb2DMuX',
           'makeb2DsMuX',
           'makeb2DX',
           'makeDstar',
           'TOSFilter',
           'confdict')

confdict = {
    ##### global settings
    "prescales"     : {"b2DsPi_PhiPi_fakes":0.1,
                       "b2D0eX":1.0}
    ,"GEC_nLongTrk" : 250 # adimensional
    ,"TTSpecs"      : {'Hlt1.*Track.*Decision%TOS':0,'Hlt2Topo(2|3|4)Body.*Decision%TOS':0,'Hlt2.*SingleMuon.*Decision%TOS':0,"Hlt2Global%TIS":0} 
    ,"HLT_FILTER"   : "HLT_PASS_RE('Hlt2.*SingleMuon.*Decision') | HLT_PASS_RE('Hlt2Topo(2|3|4)Body.*Decision')"
    ##### daughter particles
    ,"TRGHOSTPROB"   : 0.5   # adimensional
    ,"TRCHI2"        : 4     # adimensional
    ,"MuonGHOSTPROB" : 0.5   # adimensional
    ,"MINIPCHI2"     : 4.0   # adimensiional
    ,"ProtonPIDp"    : 0.0   # adimensiional 
    ,"KaonPIDK"      : -5.0  # adimensiional
    ,"PionPIDK"      : 20.0  # adimensiional
    ,"MuonPIDmu"     : 0.0   # adimensiional
    ,"ElectronPIDe"  : 0.0   # adimensiional
    ,"MuonIPCHI2"    : 4.00  # adimensiional
    ,"MuonPT"        : 800.0 # MeV
    ,"HadronPT"      : 250.0 # MeV
    ,"MuonP"         : 6.0   # GeV
    ,"HadronP"       : 2.0   # GeV
    ,"ProtonP"       : 9.0   # GeV
    ###### charm combination
    ,"D_BPVDIRA"     : 0.99  # adimensiional
    ,"D_FDCHI2"      : 25.0  # adimensiional
    ,"D_MassWin"     : 80.0  # MeV
    ,"D_AMassWin"    : 90.0  # MeV
    ,"D_VCHI2DOF"    : 6.0   # adimensiional
    ,"D_DocaChi2Max" : 20   # adimensiional
    ###### D-mu combination
    ,"B_DIRA"         : 0.999  #adimensiional
    ,"BVCHI2DOF"      : 6.0    # adimensiional
    ,"B_D_DZ"         : -0.05  #mm
    ,"BMassMin"       : 2.2 #GeV
    ,"BMassMax"       : 8.0 #GeV
    ,"B_DocaChi2Max"  : 10 #adimensiional
    ###### For D* decays
    ,"Dstar_Chi2"       :  8.0 ## unitless
    ,"Dstar_SoftPion_PIDe" : 2. ## unitless
    ,"Dstar_SoftPion_PT" : 180. ## MeV ###
    ,"Dstar_wideDMCutLower" : 0. ## MeV
    ,"Dstar_wideDMCutUpper" : 170. ## MeV,
    }

class B2DMuNuXAllLinesConf(LineBuilder) :
    
    __configuration_keys__ = (
        "prescales"
        ,"GEC_nLongTrk"
        ,"HLT_FILTER"
        ,"TRGHOSTPROB"
        ,"TRCHI2"
        ,"MuonGHOSTPROB"
        ,"MINIPCHI2"
        ,"ProtonPIDp"
        ,"KaonPIDK"
        ,"PionPIDK"
        ,"MuonIPCHI2"    
        ,"MuonPT"        
        ,"HadronPT"
        ,"D_BPVDIRA"        
        ,"D_FDCHI2"      
        ,"D_MassWin"     
        ,"D_AMassWin"    
        ,"D_VCHI2DOF"    
        ,"MuonPIDmu"         
        ,"ElectronPIDe"         
        ,"B_DIRA"         
        ,"BVCHI2DOF"     
        ,"B_D_DZ"
        ,"D_DocaChi2Max"
        ,"Dstar_Chi2"       
        ,"Dstar_SoftPion_PIDe" 
        ,"Dstar_SoftPion_PT" 
        ,"Dstar_wideDMCutLower" 
        ,"Dstar_wideDMCutUpper" 
        ,"MuonP"
        ,"HadronP"
        ,"ProtonP"
        ,"BMassMin"
        ,"BMassMax"
        ,"B_DocaChi2Max"  
        ,"TTSpecs"
        )
    
    __confdict__={}
        
    def __init__(self, name, config) :

        LineBuilder.__init__(self, name, config)
        self.__confdict__=config

        ####################### BASIC FINAL STATE PARTICLE SELECTIONS ##########################
        
        self.HadronCuts = "(P>%(HadronP)s*GeV) & (PT > %(HadronPT)s *MeV)"\
            "& (TRCHI2DOF < %(TRCHI2)s)"\
            "& (TRGHOSTPROB < %(TRGHOSTPROB)s)"\
            "& (MIPCHI2DV(PRIMARY)> %(MINIPCHI2)s)" % config
      
        self.MuonTrackCuts = "(PT > %(MuonPT)s *MeV) & (P> %(MuonP)s*GeV)"\
            "& (TRCHI2DOF < %(TRCHI2)s)"\
            "& (TRGHOSTPROB < %(MuonGHOSTPROB)s)"\
            "& (MIPCHI2DV(PRIMARY)> %(MuonIPCHI2)s)" %config
        
        self.selmuon = Selection("Mufor"+name,
                                 Algorithm=FilterDesktop(Code=self.MuonTrackCuts + " & (PIDmu > %(MuonPIDmu)s)" % config), 
                                 RequiredSelections = [StdLooseMuons])
        
        self.selelectron = Selection("efor"+name,
                                     Algorithm=FilterDesktop(Code=self.MuonTrackCuts + " & (PIDe > %(ElectronPIDe)s)" % config), 
                                     RequiredSelections = [StdLooseElectrons])
        
        self.selPionFakes = Selection( "FakeMufor" + name,
                                       Algorithm = FilterDesktop(Code = self.MuonTrackCuts + " & (INMUON) & (PIDmu < %(MuonPIDmu)s)" % config),  
                                       RequiredSelections = [StdLoosePions])
        
        self.selKaon = Selection( "Kfor" + name,
                                  Algorithm = FilterDesktop(Code=self.HadronCuts + " & (PIDK> %(KaonPIDK)s)" % config), 
                                  RequiredSelections = [StdLooseKaons])
        
        self.selPion = Selection( "Pifor" + name,
                                  Algorithm = FilterDesktop(Code=self.HadronCuts + " & (PIDK< %(PionPIDK)s)" % config),
                                  RequiredSelections = [StdLoosePions])
        
        self.selProton = Selection( "ProtonsFor" + name,
                                    Algorithm = FilterDesktop(Code=self.HadronCuts + " & (P>%(ProtonP)s*GeV) & (PIDp > %(ProtonPIDp)s)" % config),
                                    RequiredSelections = [StdLooseProtons])
        
        
        ####################### D0 -> HH LINES (inc D*->D0pi) ###############################
        
        # comments
        # try to copy the same requirements as the previous stripping
        D02HH_CONFIG = config.copy()
        D02HH_CONFIG["B_D_DZ"] = -9999
        D02HH_CONFIG["CharmDaugCuts"] = {"K+":"(PIDK > 4) & (PT > 300*MeV)",
                                         "pi+":"(PIDK < 10) & (PT > 300*MeV)"}
        D02HH_CONFIG["ExtraMuonCuts"] = "(PT>1.2*GeV) & (MIPCHI2DV(PRIMARY)> 9.0)" % config 
        D02HH_CONFIG["CharmComboCuts"] = "(ADAMASS('D0') < %(D_AMassWin)s *MeV)"\
            "& (ACHILD(PT,1)+ACHILD(PT,2) > 1400.*MeV) & (ADOCACHI2CUT( %(D_DocaChi2Max)s, ''))" % config
        D02HH_CONFIG["CharmMotherCuts"] = "(ADMASS('D0') < %(D_MassWin)s *MeV) & (VFASPF(VCHI2/VDOF) < %(D_VCHI2DOF)s) " \
            "& (BPVVDCHI2 > %(D_FDCHI2)s) &  (BPVDIRA> %(D_BPVDIRA)s)"  % config
        
        self.b2D0MuXLine = makeb2DMuXNEW(name,
                                         'b2D0MuX',
                                         ['[B- -> D0 mu-]cc','[B+ -> D0 mu+]cc'],
                                         ['[D0 -> K- pi+]cc'],
                                         D02HH_CONFIG,
                                         [self.selKaon, self.selPion],self.selmuon)

        
        D02HH_CONFIG_Ele = D02HH_CONFIG.copy()
        D02HH_CONFIG_Ele["ExtraElectronCuts"] = "(PT>1.2*GeV) & (MIPCHI2DV(PRIMARY)> 9.0)" % config 
        D02HH_CONFIG_Ele["B_D_DZ"] = 0.0
        self.b2D0eXLine = makeb2DMuXNEW(name,
                                        'b2D0eX',
                                        ['[B- -> D0 e-]cc'],
                                        ['[D0 -> K- pi+]cc'],
                                        D02HH_CONFIG_Ele,
                                        [self.selKaon, self.selPion],self.selelectron)
        
        self.b2D0MuXKKLine = makeb2DMuXNEW(name,
                                           'b2D0MuXKK',
                                           ['[B- -> D0 mu-]cc','[B+ -> D0 mu+]cc'],
                                           ['D0 -> K- K+'],
                                           D02HH_CONFIG,
                                           [self.selKaon],self.selmuon)
        
        self.b2D0MuXpipiLine = makeb2DMuXNEW(name,
                                             'b2D0MuXpipi',
                                             ['[B- -> D0 mu-]cc','[B+ -> D0 mu+]cc'],
                                             ['D0 -> pi- pi+'],
                                             D02HH_CONFIG,
                                             [self.selPion],self.selmuon)
        
        self.registerLine(self.b2D0MuXLine)        
        self.registerLine(self.b2D0eXLine)        
        self.registerLine(self.b2D0MuXKKLine)        
        self.registerLine(self.b2D0MuXpipiLine)        
                
        ####################### D+ -> HHH LINES ###############################
        D2HHH_CONFIG = config.copy()
        D2HHH_CONFIG["B_D_DZ"] = -0.1
        D2HHH_CONFIG["PhiMassMin"] = 979.455 #MeV
        D2HHH_CONFIG["PhiMassMax"] = 1059.455 #MeV
        D2HHH_CONFIG["KStarMassMin"] = 805.94 #MeV
        D2HHH_CONFIG["KStarMassMax"] = 985.94 #MeV
        D2HHH_CONFIG["BMassMin"] = 0
        D2HHH_CONFIG["BMassMax"] = 9999
        D2HHH_CONFIG["ExtraMuonCuts"] = "(MIPCHI2DV(PRIMARY)> 9) & (PT > 1000*MeV)"
        D2HHH_CONFIG["CharmComboCuts"] = "(DAMASS('D_s+') < %(D_AMassWin)s *MeV) & (DAMASS('D+')> -%(D_AMassWin)s *MeV)"\
            "& (ACHILD(PT,1)+ACHILD(PT,2)+ACHILD(PT,3) > 1800.*MeV) & (ADOCACHI2CUT( %(D_DocaChi2Max)s, ''))" % config
        D2HHH_CONFIG["CharmMotherCuts"] = "(DMASS('D_s+') < %(D_MassWin)s *MeV) & (DMASS('D+')> -%(D_AMassWin)s *MeV)"\
            "& (VFASPF(VCHI2/VDOF) < %(D_VCHI2DOF)s) & (BPVVDCHI2 > %(D_FDCHI2)s)" % config
        
        ### D+ -> K- pi+ pi+
        D2HHH_CONFIG_K2Pi = D2HHH_CONFIG.copy()
        D2HHH_CONFIG_K2Pi["CharmComboCuts"] += "& (ADAMASS('D+') < %(D_AMassWin)s *MeV)" % config
        D2HHH_CONFIG_K2Pi["CharmMotherCuts"] += "& (ADMASS('D+') < %(D_MassWin)s *MeV)" % config
        self.b2DpMuXLine = makeb2DMuXNEW(name,
                                         'b2DpMuX',
                                         [ '[B0 -> D- mu+]cc', '[B0 -> D- mu-]cc' ],
                                         [ '[D+ -> K- pi+ pi+]cc' ],
                                         D2HHH_CONFIG_K2Pi,
                                         [self.selKaon, self.selPion],self.selmuon)
        
        ### D(s)+ -> K+ K- pi+
        D2HHH_CONFIG_KKPi = D2HHH_CONFIG.copy()
        self.b2DsMuXLine = makeb2DMuXNEW(name,
                                         'b2DsMuX',
                                         [ '[B0 -> D- mu+]cc', '[B0 -> D- mu-]cc' ],
                                         [ '[D+ -> K+ K- pi+]cc' ],
                                         D2HHH_CONFIG,
                                         [self.selKaon, self.selPion],self.selmuon)
        
        ### Ds+ -> pi+ pi- pi+
        D2HHH_CONFIG_3Pi = D2HHH_CONFIG.copy()
        D2HHH_CONFIG_3Pi["CharmDaugCuts"] = {"pi+":"(PIDK < 4) & (PT > 380*MeV) & (MIPCHI2DV(PRIMARY)> 9)"}
        D2HHH_CONFIG_3Pi["BMassMin"] = 2.7 # GeV
        D2HHH_CONFIG_3Pi["BMassMax"] = 5.3 # GeV
        D2HHH_CONFIG_3Pi["B_D_DZ"]   = 0.05 #mm
        D2HHH_CONFIG_3Pi["CharmComboCuts"] += "& (ADAMASS('D+') < %(D_AMassWin)s *MeV)" % config
        D2HHH_CONFIG_3Pi["CharmMotherCuts"] += "& (ADMASS('D+') < %(D_MassWin)s *MeV)" % config
        self.b2Ds3PiMuXLine = makeb2DMuXNEW(name,
                                            'b2Ds3PiMuX',
                                            [ '[B0 -> D- mu+]cc', '[B0 -> D- mu-]cc' ],
                                            [ '[D+ -> pi+ pi- pi+]cc' ],
                                            D2HHH_CONFIG,
                                            [self.selPion],self.selmuon)
        
        ### D(s)+ -> phi(KK)pi
        D2HHH_CONFIG_PhiPi = D2HHH_CONFIG.copy()
        D2HHH_CONFIG_PhiPi["CharmExtraComboCuts"]  = "& (AM12 > (%(PhiMassMin)s - 10) *MeV) & (AM12 < (%(PhiMassMax)s + 10) *MeV)" % D2HHH_CONFIG
        D2HHH_CONFIG_PhiPi["CharmExtraMotherCuts"] = "& (M12 > %(PhiMassMin)s *MeV) & (M12 < %(PhiMassMax)s *MeV)" % D2HHH_CONFIG
        D2HHH_CONFIG_PhiPi["HLT_FILTER"] +=  "| HLT_PASS_RE('Hlt2.*IncPhi.*Decision')"
        D2HHH_CONFIG_PhiPi["TTSpecs"].update({'Hlt2.*IncPhi.*Decision%TOS':0})
        self.b2DsPhiPiMuXLine = makeb2DMuXNEW(name,
                                              'b2DsPhiPiMuX',
                                              [ '[B0 -> D- mu+]cc', '[B0 -> D- mu-]cc' ],
                                              [ '[D+ -> K+ K- pi+]cc' ],
                                              D2HHH_CONFIG_PhiPi,
                                              [self.selKaon, self.selPion],self.selmuon)

        ### D(s)+ -> K*(K-pi+)K+
        D2HHH_CONFIG_KStarK = D2HHH_CONFIG.copy()
        D2HHH_CONFIG_KStarK["CharmExtraComboCuts"]  = "& (AM23 > (%(KStarMassMin)s - 10) *MeV) & (AM23 < (%(KStarMassMax)s + 10) *MeV)" % D2HHH_CONFIG
        D2HHH_CONFIG_KStarK["CharmExtraMotherCuts"] = "& (M23 > %(KStarMassMin)s *MeV) & (M23 < %(KStarMassMax)s *MeV)" % D2HHH_CONFIG
        self.b2DsKStarKMuXLine = makeb2DMuXNEW(name,
                                               'b2DsKStarKMuX',
                                               [ '[B0 -> D- mu+]cc', '[B0 -> D- mu-]cc' ],
                                               [ '[D+ -> K+ K- pi+]cc' ],
                                               D2HHH_CONFIG_KStarK,
                                               [self.selKaon, self.selPion],self.selmuon)
        
        ### D(s)+ -> phi(KK)pi with fake muon
        D2HHH_CONFIG_PhiPiFakes = D2HHH_CONFIG_PhiPi.copy()
        D2HHH_CONFIG_PhiPiFakes["CharmExtraComboCuts"]  = "& (ADAMASS('D_s+') < %(D_AMassWin)s*MeV)" %D2HHH_CONFIG_PhiPiFakes
        D2HHH_CONFIG_PhiPiFakes["CharmExtraMotherCuts"] = "& (ADMASS('D_s+') < %(D_MassWin)s*MeV)" %D2HHH_CONFIG_PhiPiFakes
        self.b2DsPhiPiMuXFakesLine = makeb2DMuXNEW(name,
                                                   'b2DsPi_PhiPi_fakes',
                                                   [ '[B0 -> D- pi+]cc', '[B0 -> D- pi-]cc' ],
                                                   [ '[D+ -> K+ K- pi+]cc' ],
                                                   D2HHH_CONFIG_PhiPiFakes,
                                                   [self.selKaon, self.selPion],self.selPionFakes)
        
        self.registerLine(self.b2DpMuXLine)        
        self.registerLine(self.b2DsMuXLine)        
        self.registerLine(self.b2DsKStarKMuXLine)        
        self.registerLine(self.b2DsPhiPiMuXLine)   
        self.registerLine(self.b2DsPhiPiMuXFakesLine)   
        self.registerLine(self.b2Ds3PiMuXLine)        
        
        ####################### Lc+ -> pHH LINES ###############################
        LC2PHH_CONFIG = config.copy()
        LC2PHH_CONFIG["ExtraMuonCuts"] = "(PT > 1000*MeV) & (MIPCHI2DV(PRIMARY)> 9)"
        LC2PHH_CONFIG["CharmComboCuts"] = "(ADAMASS('Lambda_c+') < %(D_AMassWin)s *MeV)"\
            "& (APT > 2000*MeV) & (ADOCACHI2CUT( %(D_DocaChi2Max)s, ''))" % LC2PHH_CONFIG
        LC2PHH_CONFIG["CharmMotherCuts"] = "(ADMASS('Lambda_c+') < %(D_MassWin)s *MeV) & (VFASPF(VCHI2/VDOF) < %(D_VCHI2DOF)s) " \
            "& (BPVVDCHI2 > %(D_FDCHI2)s) & (PT>2100.*MeV) & (BPVDIRA> %(D_BPVDIRA)s)"  % LC2PHH_CONFIG
        self.lb2LcMuXLine = makeb2DMuXNEW(name,
                                          "b2LcMuX",
                                          [ '[Lambda_b0 -> Lambda_c+ mu-]cc', '[Lambda_b0 -> Lambda_c+ mu+]cc'],
                                          [ '[Lambda_c+ -> K- p+ pi+]cc' ],
                                          LC2PHH_CONFIG,
                                          [self.selProton,self.selKaon,self.selPion],self.selmuon)
        self.registerLine(self.lb2LcMuXLine)
            

###################### FUNCTION TO MAKE AN ENTIRE B->D MU X DECAY CANDIDATE  ########################
def makeb2DMuXNEW(module_name,
                  name,
                  BDecays,
                  DDecays,
                  CONFIG,
                  CHARM_DAUGHTERS,
                  MUON):

    DEFAULT_GECs = { "Code":"( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) < %(GEC_nLongTrk)s )" %CONFIG,
                     "Preambulo": ["from LoKiTracks.decorators import *"]}
    
    DEFAULT_HLT = CONFIG["HLT_FILTER"]
    
    CHARM_DaugCuts = {}
    CHARM_ComboCuts = CONFIG["CharmComboCuts"]
    CHARM_MotherCuts = CONFIG["CharmMotherCuts"]
    
    if "CharmDaugCuts" in CONFIG.keys():
        CHARM_DaugCuts = CONFIG["CharmDaugCuts"]
    if "CharmExtraComboCuts" in CONFIG.keys():
        CHARM_ComboCuts += CONFIG["CharmExtraComboCuts"]
    if "CharmExtraMotherCuts" in CONFIG.keys():
        CHARM_MotherCuts += CONFIG["CharmExtraMotherCuts"]
    
    CHARM = Selection("CharmSelFor"+name+module_name,
                      Algorithm=CombineParticles(DecayDescriptors = DDecays,
                                                 DaughtersCuts = CHARM_DaugCuts,
                                                 CombinationCut = CHARM_ComboCuts,
                                                 MotherCut = CHARM_MotherCuts),
                      RequiredSelections = CHARM_DAUGHTERS)

    USED_CHARM = CHARM
    if "D*" in BDecays:
        DST = makeDstar("CharmSelDstFor"+name+module_name,CHARM,CONFIG)
        USED_CHARM = DST

    B_combinationCut = "(AM > %(BMassMin)s*GeV) & (AM < %(BMassMax)s*GeV) & (ADOCACHI2CUT( %(B_DocaChi2Max)s, ''))" %CONFIG
    B_motherCut = " (MM>%(BMassMin)s*GeV) & (MM<%(BMassMax)s*GeV) &  (VFASPF(VCHI2/VDOF)< %(BVCHI2DOF)s) & (BPVDIRA> %(B_DIRA)s)  " \
        "& (MINTREE(((ABSID=='D+') | (ABSID=='D0') | (ABSID=='Lambda_c+')) , VFASPF(VZ))-VFASPF(VZ) > %(B_D_DZ)s *mm ) " %CONFIG
    if "ExtraComboCuts" in CONFIG.keys():
        B_combinationCut += CONFIG["ExtraComboCuts"]
    if "ExtraMotherCuts" in CONFIG.keys():
        B_motherCut += CONFIG["ExtraMotherCuts"]
        
    B_DaugCuts = {}
    if "ExtraMuonCuts" in CONFIG.keys():
        B_DaugCuts = {"mu+":CONFIG["ExtraMuonCuts"]}
    if "ExtraElectronCuts" in CONFIG.keys():
        B_DaugCuts = {"e+":CONFIG["ExtraElectronCuts"]}
    _B = CombineParticles(DecayDescriptors = BDecays,
                          DaughtersCuts = B_DaugCuts,
                          CombinationCut = B_combinationCut,
                          MotherCut = B_motherCut)
                     
    BSel = Selection ("BSelFor"+name+module_name,
                      Algorithm = _B,
                      RequiredSelections = [MUON,USED_CHARM])
    
    ### invert the order for the fakes line
    ### to be more efficient
    if "fakes" in name:
        BSel.RequiredSelections = [USED_CHARM,MUON]
    
    BSelTOS = TOSFilter( "BSelFor"+name+module_name+"TOS"
                         ,BSel
                         ,CONFIG["TTSpecs"])
    
    debug = False
    if debug:
        print [name,DEFAULT_HLT,CHARM_DaugCuts,Charm_ComboCuts,CHARM_MotherCuts,B_DaugCuts,B_combinationCut,B_motherCut]
    _prescale = 1.0
    if name in CONFIG["prescales"].keys():
        _prescale = CONFIG["prescales"][name]

    return StrippingLine(name + module_name + 'Line', 
                         HLT = DEFAULT_HLT,
                         FILTER=DEFAULT_GECs,
                         prescale = _prescale,
                         selection = BSelTOS)

########### HELP WITH MAKING A DSTAR ########################
def makeDstar(_name, inputD0,CONFIG) : 
    _softPi = DataOnDemand(Location = 'Phys/StdAllLoosePions/Particles')
    _inputD0_conj = Selection("SelConjugateD0For"+_name,
                             Algorithm = ConjugateNeutralPID('ConjugateD0For'+_name),
                             RequiredSelections = [inputD0])
    _cutsSoftPi = '( PT > %(Dstar_SoftPion_PT)s *MeV )' % CONFIG
    _cutsDstarComb = '(AM - ACHILD(M,1) + 5 > %(Dstar_wideDMCutLower)s *MeV) & (AM - ACHILD(M,1) - 5 < %(Dstar_wideDMCutUpper)s *MeV)' % CONFIG
    _cutsDstarMoth_base = '(VFASPF(VCHI2/VDOF) < %(Dstar_Chi2)s )' % CONFIG
    _cutsDstarMoth_DM = '(M - CHILD(M,1) > %(Dstar_wideDMCutLower)s *MeV) & (M - CHILD(M,1) < %(Dstar_wideDMCutUpper)s *MeV)' % CONFIG
    _cutsDstarMoth = '(' + _cutsDstarMoth_base + ' & ' + _cutsDstarMoth_DM + ')'
    _Dstar = CombineParticles( DecayDescriptor = "[D*(2010)+ -> D0 pi+]cc",
                               DaughtersCuts = { "pi+" : _cutsSoftPi },
                               CombinationCut = _cutsDstarComb,
                               MotherCut = _cutsDstarMoth)
    return Selection (name = "Sel"+_name,Algorithm = _Dstar,RequiredSelections = [inputD0,_inputD0_conj] + [_softPi])

########## TISTOS FILTERING ##################################
def TOSFilter( name = None, sel = None, trigger = None ):
    if len(trigger) == 0:
        return sel
    from Configurables import TisTosParticleTagger
    _filter = TisTosParticleTagger(name+"_TriggerTos")
    _filter.TisTosSpecs = trigger
    _sel = Selection("Sel" + name + "_TriggerTos", RequiredSelections = [ sel ], Algorithm = _filter )
    return _sel



