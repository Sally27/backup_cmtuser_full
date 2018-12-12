# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/32101200.py generated: Wed, 25 Jan 2017 15:25:18
#
# Event Type: 32101200
#
# ASCII decay Descriptor: [Sigma+ -> p+ gamma]cc
#
from Configurables import Generation
Generation().EventType = 32101200
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Sigma+_pgamma=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 3222,-3222 ]
