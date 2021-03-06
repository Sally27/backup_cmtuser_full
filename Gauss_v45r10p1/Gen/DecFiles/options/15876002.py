# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/15876002.py generated: Wed, 25 Jan 2017 15:25:16
#
# Event Type: 15876002
#
# ASCII decay Descriptor: [Lambda_b0 -> (Lambda_c(2625)+ -> (Lambda_c+ -> p+ K- pi+) pi+ pi-) mu- anti-nu_mu]cc
#
from Configurables import Generation
Generation().EventType = 15876002
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Lc2625munu,pKpi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "LHCbAcceptance"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
