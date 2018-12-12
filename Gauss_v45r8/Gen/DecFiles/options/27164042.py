# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/27164042.py generated: Fri, 27 Mar 2015 15:48:05
#
# Event Type: 27164042
#
# ASCII decay Descriptor: {[ D*_2(2460)0 -> (D+ -> K- pi+ pi+) pi- ]cc}
#
from Configurables import Generation
Generation().EventType = 27164042
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D2st_m=2300MeV_D+Pi,D+2KPiPi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 425,-425 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "D*_2(2460)0 170 425 0.0 2.3 4.388079327e-24 D_2*0 425 0.29080982","D*_2(2460)~0 166 -425 0.0 2.3 4.388079327e-24 anti-D_2*0 -425 0.29080982" ]
