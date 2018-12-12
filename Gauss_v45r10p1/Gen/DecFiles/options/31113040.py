# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/31113040.py generated: Wed, 25 Jan 2017 15:25:32
#
# Event Type: 31113040
#
# ASCII decay Descriptor: [tau- -> mu- K+ K-]cc
#
from Configurables import Generation
Generation().EventType = 31113040
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/tau_mu-K+K-=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 15,-15 ]
