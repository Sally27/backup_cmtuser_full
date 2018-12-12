# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/21263000.py generated: Fri, 27 Mar 2015 16:10:01
#
# Event Type: 21263000
#
# ASCII decay Descriptor: [D+ => K+ K- pi+]cc
#
from Configurables import Generation
Generation().EventType = 21263000
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D+_K+K-pi+=res,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 411,-411 ]
