# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/15898002.py generated: Wed, 25 Jan 2017 15:25:32
#
# Event Type: 15898002
#
# ASCII decay Descriptor: [Lambda_b0 -> (D*- -> (D0 -> K- mu+ nu_mu) pi-) (Lambda_c(2593)+ -> (Sigma_c0 -> (Lambda_c+ -> p+ K- pi+) pi-) pi+)]cc
#
from Configurables import Generation
Generation().EventType = 15898002
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Lc2593Dst,Lcpipi,ppiK,semileptonic=DecProdCut,cocktail.dec"
Generation().SignalPlain.CutTool = "LHCbAcceptance"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
