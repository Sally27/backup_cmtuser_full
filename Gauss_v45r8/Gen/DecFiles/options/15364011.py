# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/15364011.py generated: Fri, 27 Mar 2015 15:48:00
#
# Event Type: 15364011
#
# ASCII decay Descriptor: [Lb_b0 -> (Lambda_c+ -> p+ K- pi+) K-]cc
#
from Configurables import Generation
Generation().EventType = 15364011
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_LcK,pKpi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
