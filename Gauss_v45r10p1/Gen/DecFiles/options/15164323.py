# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/15164323.py generated: Wed, 25 Jan 2017 15:25:29
#
# Event Type: 15164323
#
# ASCII decay Descriptor: [Lambda_b0 -> (anti-D0 -> pi+ pi-) (Sigma0 -> (Lambda -> p+ pi-) gamma)]cc
#
from Configurables import Generation
Generation().EventType = 15164323
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_antiD0Sigma,pipiLambdagamma,ppi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
