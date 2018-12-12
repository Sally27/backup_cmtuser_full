# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11164095.py generated: Fri, 27 Mar 2015 15:48:07
#
# Event Type: 11164095
#
# ASCII decay Descriptor: {[[B0]nos => (D_s2*- -> K- D~0) K+ ]cc, [[B0]os => (D_s2*+ -> K+ D0) K- ]cc}
#
from Configurables import Generation
Generation().EventType = 11164095
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Ds2573K,D0K,Kpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LHCbAcceptance"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
