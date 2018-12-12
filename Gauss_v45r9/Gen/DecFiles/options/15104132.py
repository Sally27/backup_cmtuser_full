# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/15104132.py generated: Fri, 27 Mar 2015 16:10:16
#
# Event Type: 15104132
#
# ASCII decay Descriptor: [Lambda_b0  -> K+ K- (Lambda0 -> p+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 15104132
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_LambdaKK=sqDalitz,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
