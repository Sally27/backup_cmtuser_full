# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11196080.py generated: Fri, 27 Mar 2015 15:47:58
#
# Event Type: 11196080
#
# ASCII decay Descriptor: [B0 -> (D*(2010)+ -> (D0 -> K- pi+) pi+) (D*(2010)- -> (D~0 -> K+ pi-) pi-)]cc
#
from Configurables import Generation
Generation().EventType = 11196080
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dst-Dst+,D0pi-,Kpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
