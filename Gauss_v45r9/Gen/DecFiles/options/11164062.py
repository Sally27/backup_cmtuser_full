# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11164062.py generated: Fri, 27 Mar 2015 16:10:07
#
# Event Type: 11164062
#
# ASCII decay Descriptor: {[[B0]nos => p+ p~- (D~0 -> K+ pi-)]cc, [[B0]os => p+ p~- (D0 -> K- pi+)]cc}
#
from Configurables import Generation
Generation().EventType = 11164062
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D0ppbar,Kpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
