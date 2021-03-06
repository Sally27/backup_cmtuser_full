# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/16264410.py generated: Wed, 25 Jan 2017 15:25:34
#
# Event Type: 16264410
#
# ASCII decay Descriptor: [Sigma_b0 -> (Xi_b0 -> Xic+ pi-) pi0]cc
#
from Configurables import Generation
Generation().EventType = 16264410
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xibpr0_Xibpi0,Xicpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5212,-5212 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ " Sigma_b0   112   5212 0.0  5.93320  6.000000e-020       Sigma_b0   5212  1.000000e-004", " Sigma_b~0  113  -5212  0.0  5.93320  6.000000e-020  anti-Sigma_b0  -5212  1.000000e-004", " Xi_b0   124   5232  0.0  5.7918  1.480000e-012       Xi_b0   5232  0.000000e+000", " Xi_b~0  125  -5232  0.0  5.7918  1.480000e-012  anti-Xi_b0  -5232  0.000000e+000" ]
