# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/15102228.py generated: Wed, 25 Jan 2017 15:25:15
#
# Event Type: 15102228
#
# ASCII decay Descriptor: [Lambda_b0 -> (Lambda(1670)0 -> p+ K-) gamma]cc
#
from Configurables import Generation
Generation().EventType = 15102228
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_gammaLambda1670=pol,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
