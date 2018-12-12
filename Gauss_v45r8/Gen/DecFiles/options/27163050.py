# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/27163050.py generated: Fri, 27 Mar 2015 15:48:13
#
# Event Type: 27163050
#
# ASCII decay Descriptor: {[ D*_2(2460)+ -> (D0 -> K- pi+) pi+ ]cc}
#
from Configurables import Generation
Generation().EventType = 27163050
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D2st_m=2300MeV_D0Pi,D02KPi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 415,-415 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "D*_2(2460)+ 162 415 1.0 2.3 4.388079327e-24 D_2*+ 415 0.29558982","D*_2(2460)- 158 -415 -1.0 2.3 4.388079327e-24 D_2*- -415 0.29558982" ]
