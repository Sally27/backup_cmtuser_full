# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/25103021.py generated: Wed, 25 Jan 2017 15:25:33
#
# Event Type: 25103021
#
# ASCII decay Descriptor: [Lambda_c+ -> p+ (phi(1020) -> K+ K-)]cc
#
from Configurables import Generation
Generation().EventType = 25103021
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Betac_pphi,KK=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 4122,-4122 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "Lambda_c+  62  4122  1.0  2.428 4.400000e-013   Lambda_c+  4122  0", "Lambda_c~-  63 -4122 -1.0  2.428 4.400000e-013  anti-Lambda_c-  -4122   0." ]
