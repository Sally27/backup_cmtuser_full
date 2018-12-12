# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11296420.py generated: Fri, 27 Mar 2015 16:10:14
#
# Event Type: 11296420
#
# ASCII decay Descriptor: [B0 -> (X_1(3872) ->  (D0 -> K- pi+) (anti-D*0 -> (anti-D0 -> K+ pi-) pi0) ) K+ pi-]cc
#
from Configurables import Generation
Generation().EventType = 11296420
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_X38721++Kpi,D0barDst0,D0D0barPi0,Kpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
