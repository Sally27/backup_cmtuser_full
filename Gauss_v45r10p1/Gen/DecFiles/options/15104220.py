# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/15104220.py generated: Wed, 25 Jan 2017 15:25:25
#
# Event Type: 15104220
#
# ASCII decay Descriptor: [Lambda_b0 -> (Lambda_c+ -> p+ KS0 (pi0 -> gamma gamma) ) K-]cc
#
from Configurables import Generation
Generation().EventType = 15104220
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_LambdacK,pKSpi0=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
