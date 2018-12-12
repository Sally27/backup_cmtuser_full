# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/25105101.py generated: Wed, 25 Jan 2017 15:25:14
#
# Event Type: 25105101
#
# ASCII decay Descriptor: [Lambda_c+ -> (Xi- -> (Lambda0 -> p+ pi-) pi-) K+ pi+]cc
#
from Configurables import Generation
Generation().EventType = 25105101
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lc_XiKpi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 4122,-4122 ]
