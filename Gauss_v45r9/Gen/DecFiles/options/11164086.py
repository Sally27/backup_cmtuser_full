# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11164086.py generated: Fri, 27 Mar 2015 16:10:16
#
# Event Type: 11164086
#
# ASCII decay Descriptor: {[[B0]nos => K+ K- (D~0 -> K+ pi-)]cc, [[B0]os => K- K+ (D0 -> K- pi+)]cc}
#
from Configurables import Generation
Generation().EventType = 11164086
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D0KK,Kpi=sqDalitz,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
