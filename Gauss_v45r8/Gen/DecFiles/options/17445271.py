# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/17445271.py generated: Fri, 27 Mar 2015 15:48:13
#
# Event Type: 17445271
#
# ASCII decay Descriptor: [B*_2+ -> (B0 -> (K*0 -> K+ pi-) (J/psi(1S) -> mu+ mu- )) pi+]cc, [B*_2+ -> (B0 -> (D- -> K+ pi- pi+) pi+) pi+]cc, [B*_2+ -> (B0 -> (D*- -> (D~0 -> {K- pi+, K- pi+ pi- pi+}) pi-)  pi+) pi+]cc, [B*_2+ -> (B0 -> (D- -> K+ pi- pi+) pi+ pi- pi+) pi+]cc, [B*_2+ -> (B0 -> (D*- -> (D~0 -> {K- pi+, K- pi+ pi- pi+}) pi-)  pi+ pi- pi+) pi+]cc, [B*_2+ -> ( B*0 -> (B0 -> (K*0 -> K+ pi-) (J/psi(1S) -> mu+ mu- )) gamma ) pi+]cc, [B*_2+ -> ( B*0 -> (B0 -> (D- -> K+ pi- pi+) pi+) gamma ) pi+]cc, [B*_2+ -> ( B*0 -> (B0 -> (D*- -> (D~0 -> {K- pi+, K- pi+ pi- pi+}) pi-)  pi+) gamma ) pi+]cc, [B*_2+ -> ( B*0 -> (B0 -> (D- -> K+ pi- pi+) pi+ pi- pi+) gamma ) pi+]cc, [B*_2+ -> ( B*0 -> (B0 -> (D*- -> (D~0 -> {K- pi+, K- pi+ pi- pi+}) pi-)  pi+ pi- pi+) gamma ) pi+]cc
#
from Configurables import Generation
Generation().EventType = 17445271
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/B2st+_Bdstpi,Bdpi,JpsiKst=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 525,-525 ]
