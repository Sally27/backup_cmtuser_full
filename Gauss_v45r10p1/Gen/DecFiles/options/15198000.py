# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/15198000.py generated: Wed, 25 Jan 2017 15:25:18
#
# Event Type: 15198000
#
# ASCII decay Descriptor: [Lambda_b0 -> (K*0 -> K+ pi-) Lambda_c+ D-]cc
#
from Configurables import Generation
Generation().EventType = 15198000
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_LcDKst0,pKpi,Kpipi,Kpi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
