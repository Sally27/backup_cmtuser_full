# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/17445241.py generated: Wed, 25 Jan 2017 15:25:18
#
# Event Type: 17445241
#
# ASCII decay Descriptor: [B_1(L)+ -> ( B*0 -> (B0 -> (K*0 -> K+ pi-) (J/psi(1S) -> mu+ mu- )) gamma ) pi+]cc, [B_1(L)+ -> ( B*0 -> (B0 -> (D- -> K+ pi- pi+) pi+) gamma ) pi+]cc, [B_1(L)+ -> ( B*0 -> (B0 -> (D*- -> (D~0 -> {K- pi+, K- pi+ pi- pi+}) pi-)  pi+) gamma ) pi+]cc, [B_1(L)+ -> ( B*0 -> (B0 -> (D- -> K+ pi- pi+) pi+ pi- pi+) gamma ) pi+]cc, [B_1(L)+ -> ( B*0 -> (B0 -> (D*- -> (D~0 -> {K- pi+, K- pi+ pi- pi+}) pi-)  pi+ pi- pi+) gamma ) pi+]cc
#
from Configurables import Generation
Generation().EventType = 17445241
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/B1+_Bdstpi,JpsiKst=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 10523,-10523 ]
