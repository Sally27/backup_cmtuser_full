# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/15104125.py generated: Wed, 25 Jan 2017 15:25:33
#
# Event Type: 15104125
#
# ASCII decay Descriptor: [Lambda_b0  -> pi+ pi- (Lambda0 -> p+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 15104125
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Lambdapipi=sqDalitz,pipiref,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
