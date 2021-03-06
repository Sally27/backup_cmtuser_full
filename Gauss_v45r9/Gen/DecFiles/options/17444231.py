# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/17444231.py generated: Fri, 27 Mar 2015 16:10:00
#
# Event Type: 17444231
#
# ASCII decay Descriptor: [B_1(L)0 ->  ( B*+ -> (B+ -> K+ (J/psi(1S) -> mu+ mu- )) gamma ) K-]cc, [B_1(L)0 ->  ( B*+ -> (B+ -> (D~0 -> {K+ pi-, K+ pi- pi+ pi-}) pi+ ) gamma ) K-]cc, [B_1(L)0 ->  ( B*+ -> (B+ -> (D~0 -> {K+ pi-, K+ pi- pi+ pi-}) pi+ pi- pi+) gamma ) K-]cc
#
from Configurables import Generation
Generation().EventType = 17444231
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/B10_Bstpi,JpsiK=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 10513,-10513 ]
