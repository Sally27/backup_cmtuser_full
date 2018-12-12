# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/15266400.py generated: Wed, 25 Jan 2017 15:25:20
#
# Event Type: 15266400
#
# ASCII decay Descriptor: [Lambda_b0 -> (Sigma_c+ -> (Lambda_c+ -> p+ K- pi+) pi0) K- K+ pi-]cc
#
from Configurables import Generation
Generation().EventType = 15266400
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_ScKKpi,Lcpi,pKpi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
