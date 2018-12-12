# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/16265400.py generated: Wed, 25 Jan 2017 15:25:23
#
# Event Type: 16265400
#
# ASCII decay Descriptor: [Sigma_b- -> (Xi_b- -> Xic0 pi-) pi0]cc
#
from Configurables import Generation
Generation().EventType = 16265400
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xibprime_Xibminuspi0,Xic0pi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5112,-5112 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ " Sigma_b-   114   5112 -1.0  5.93506  6.000000e-020       Sigma_b-   5112  1.000000e-004", " Sigma_b~+  115  -5112  1.0  5.93506  6.000000e-020  anti-Sigma_b+  -5112  1.000000e-004", " Xi_b-   122   5132  -1.0  5.7977  1.600000e-012       Xi_b-   5132  0.000000e+000", " Xi_b~+  123  -5132  1.0  5.7977  1.600000e-012  anti-Xi_b+  -5132  0.000000e+000" ]
