# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11164073.py generated: Fri, 27 Mar 2015 15:48:08
#
# Event Type: 11164073
#
# ASCII decay Descriptor: {[[B0]nos => K+ pi- (D0 -> K+ pi-)]cc, [[B0]os => K- pi+ (D~0 -> K- pi+)]cc}
#
from Configurables import Generation
Generation().EventType = 11164073
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D0Kpi,Kpi=Sup,PHSP,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
