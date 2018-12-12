# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/40112050.py generated: Wed, 25 Jan 2017 15:25:33
#
# Event Type: 40112050
#
# ASCII decay Descriptor: (A0 -> e- mu+) (A0 -> e+ mu-)
#
from Configurables import Generation
Generation().EventType = 40112050
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/A1_emu,mA=2GeV,tA=0ps,Anarrow.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/LeptonsFromA1InAcceptance"
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "H_30 89 36 0.0   2.0 1e-20   A0 36 0.0e+00" ]
                                                                          
from Configurables import Generation                                                            
from Gaudi.Configuration import *
Generation().PileUpTool = "FixedLuminosityForRareProcess"
importOptions( "$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py" )
from Configurables import Special, Pythia8Production
Generation().addTool( Special )
Generation().Special.addTool( Pythia8Production )
## Pythia8 production commands                                                                            
Generation().Special.Pythia8Production.Commands += [
                                                    "SpaceShower:rapidityOrder = off" # pT ordering
                                                    ,"Higgs:useBSM = on" # Switch Higgs BSM on
                                                    ,"HiggsBSM:allA3 = on" # Switch H_30 (A0) production on
                                                    ,"36:mWidth = 1.e-20" #width in GeV
                                                    ,"36:m0 = 2.0" #mass in GeV
                                                    ,"36:doForceWidth = true"
                                                    ,"36:doExternalDecay = true"
                                                    ,"PartonLevel:FSR=on" # FSR by PYTHIA8 (NOT PHOTOS)
                                                    ]

from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "LeptonsFromA1InAcceptance" )
tracksInAcc = Generation().LeptonsFromA1InAcceptance
tracksInAcc.Code = " count ( isGoodA1 ) > 0 "
### - HepMC::IteratorRange::descendants   4
tracksInAcc.Preambulo += [
      "from GaudiKernel.SystemOfUnits import GeV, mrad"
    , "isA1           = ( 'H_30' == GID )"
    , "isGoodDaughterMu = ( ( ~GVEV ) & ( GTHETA < 400.0*mrad ) & ( 'mu+' == GABSID ) )"
    , "isGoodDaughterE = ( ( ~GVEV ) & ( GTHETA < 400.0*mrad ) & ( 'e-' == GABSID ) )"
    , "isGoodA1 = ( isA1 & ( GNINTREE( isGoodDaughterMu, 4 ) ==1 ) & ( GNINTREE( isGoodDaughterE, 4 ) ==1 ) )"
    ]

