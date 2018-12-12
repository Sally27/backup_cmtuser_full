# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/15164080.py generated: Fri, 27 Mar 2015 15:48:01
#
# Event Type: 15164080
#
# ASCII decay Descriptor: [Lambda_b0 -> (D0 -> K- K+) p+ K- ]cc
#
from Configurables import Generation
Generation().EventType = 15164080
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_D0pK,KK=sqDalitz,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
