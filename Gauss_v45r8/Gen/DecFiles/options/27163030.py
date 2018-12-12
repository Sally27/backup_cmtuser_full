# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/27163030.py generated: Fri, 27 Mar 2015 15:47:59
#
# Event Type: 27163030
#
# ASCII decay Descriptor: {[ D_s2*+ -> (D0 -> K- pi+) K+ ]cc}
#
from Configurables import Generation
Generation().EventType = 27163030
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds2st_m=2600MeV_D0K,D02KPi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 435,-435 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "D*_s2+ 174 435 1.0 2.6 4.388079327e-24 D_s2*+ 435 0.241483","D*_s2- 178 -435 -1.0 2.6 4.388079327e-24 D_s2*- -435 0.241483" ]
