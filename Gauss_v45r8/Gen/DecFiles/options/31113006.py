# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/31113006.py generated: Fri, 27 Mar 2015 15:48:04
#
# Event Type: 31113006
#
# ASCII decay Descriptor: [tau+ -> p+ mu+ mu-]cc
#
from Configurables import Generation
Generation().EventType = 31113006
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/tau+_p+mu+mu-=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 15,-15 ]
