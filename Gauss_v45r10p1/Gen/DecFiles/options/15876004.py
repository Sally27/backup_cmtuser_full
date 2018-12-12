# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/15876004.py generated: Wed, 25 Jan 2017 15:25:17
#
# Event Type: 15876004
#
# ASCII decay Descriptor: [Lambda_b0 -> (Lambda_c(2593)+ -> (Lambda_c+ -> p+ K- pi+) pi+ pi-) tau- anti-nu_tau]CC
#
from Configurables import Generation
Generation().EventType = 15876004
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Lc2593taunu,pKpi,taumu=DecProdCut.dec"
Generation().SignalPlain.CutTool = "LHCbAcceptance"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
