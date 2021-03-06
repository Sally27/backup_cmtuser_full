# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/15396401.py generated: Wed, 25 Jan 2017 15:25:35
#
# Event Type: 15396401
#
# ASCII decay Descriptor: [Lambda_b0 -> K- (Sigma_c+ -> (Lambda_c+ -> p+ K- pi+) pi0) (anti-D0 ->  K+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 15396401
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_ScD0K,Sc_Lcpi,D0_Kpi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
