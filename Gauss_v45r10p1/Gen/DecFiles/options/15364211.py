# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/15364211.py generated: Wed, 25 Jan 2017 15:25:32
#
# Event Type: 15364211
#
# ASCII decay Descriptor: [Lambda_b0 -> (D_s*- -> {gamma (D_s- -> K+ K- pi-), pi0 (D_s- -> K+ K- pi-)}) p+]cc
#
from Configurables import Generation
Generation().EventType = 15364211
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Dsstp,K+K-pi-=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
