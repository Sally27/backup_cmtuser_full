# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11164449.py generated: Fri, 27 Mar 2015 16:10:11
#
# Event Type: 11164449
#
# ASCII decay Descriptor: {[[B0]nos -> (D*(2007)~0 -> (D~0 -> K+ pi-) (pi0 -> gamma gamma) ) K+ pi- ]cc, [[B0]os -> (D*(2007)0 -> (D0 -> K- pi+) (pi0 -> gamma gamma) ) K- pi+ ]cc}
#
from Configurables import Generation
Generation().EventType = 11164449
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dst0Kpi,D0pi0,Kpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
