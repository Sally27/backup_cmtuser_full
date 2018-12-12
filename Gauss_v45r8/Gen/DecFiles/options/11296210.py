# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11296210.py generated: Fri, 27 Mar 2015 15:48:11
#
# Event Type: 11296210
#
# ASCII decay Descriptor: [B0 -> (X_1(3872) ->  (D0 -> K- pi+) (anti-D*0 -> (anti-D0 -> K+ pi-) gamma) ) K+ pi-]cc
#
from Configurables import Generation
Generation().EventType = 11296210
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_X38721++Kpi,D0barDst0,D0D0barGamma,Kpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
