# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/15296003.py generated: Wed, 25 Jan 2017 15:25:32
#
# Event Type: 15296003
#
# ASCII decay Descriptor: [Lambda_b0 -> (Lambda_c+ -> p+ K- pi+) (D_s- -> K+ K- pi-)]cc
#
from Configurables import Generation
Generation().EventType = 15296003
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_LcDs,pKpi,KKpi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
