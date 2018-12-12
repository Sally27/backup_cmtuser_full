# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/27495731.py generated: Wed, 25 Jan 2017 15:25:23
#
# Event Type: 27495731
#
# ASCII decay Descriptor: {[ D_s2*+ -> D0 K+, D*0 K+, D+ K_S0, D*+ K_S0 ]cc}
#
from Configurables import Generation
Generation().EventType = 27495731
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds2st_2860=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 435,-435 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "D*_s2+ 174 435 1.0 2.860 13.1642379809999994e-24 D_s2*+ 435 0.501483","D*_s2- 178 -435 -1.0 2.860 13.1642379809999994e-24 D_s2*- -435 0.501483" ]
