# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/15296300.py generated: Fri, 27 Mar 2015 16:10:01
#
# Event Type: 15296300
#
# ASCII decay Descriptor: [Lambda_b0 -> (X_1(3872) ->  (D0 -> K- pi+) (anti-D*0 -> (anti-D0 -> K+ pi-) gamma) ) (Lambda0 -> p+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 15296300
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_X38721++Lambda,D0barDst0,D0D0barGamma,Kpi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
