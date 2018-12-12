# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/15266025.py generated: Wed, 25 Jan 2017 15:25:37
#
# Event Type: 15266025
#
# ASCII decay Descriptor: [Lambda_b0 -> (Sigma_c*0 -> (Lambda_c+ -> p+ K- pi+) pi-) K- K+]cc
#
from Configurables import Generation
Generation().EventType = 15266025
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_ScstKK,Lcpi,pKpi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
