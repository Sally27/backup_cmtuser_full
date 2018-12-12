# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/21105120.py generated: Fri, 27 Mar 2015 15:48:01
#
# Event Type: 21105120
#
# ASCII decay Descriptor: [D+ -> (KS0 -> pi+ pi-) K- pi+ pi+]cc
#
from Configurables import Generation
Generation().EventType = 21105120
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D+_KsK-pi+pi+=phsp,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 411,-411 ]
