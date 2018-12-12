# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/15295005.py generated: Wed, 25 Jan 2017 15:25:37
#
# Event Type: 15295005
#
# ASCII decay Descriptor: [Lambda_b0 -> D*- (Lambda_c(2593)+ -> (Sigma_c0 -> (Lambda_c+ -> p+ K- pi+) pi-) pi+)]cc
#
from Configurables import Generation
Generation().EventType = 15295005
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Lc2593Dst,Lcpipi,ppiK=DecProdCut,cocktail,inclusive.dec"
Generation().SignalPlain.CutTool = "LHCbAcceptance"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
