# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11164442.py generated: Fri, 27 Mar 2015 15:48:06
#
# Event Type: 11164442
#
# ASCII decay Descriptor: {[[B0]nos -> (D*(2007)~0 -> (D~0 -> K+ pi-) (pi0 -> gamma gamma) ) (rho(770)0 -> pi+ pi-) ]cc, [[B0]os -> (D*(2007)0 -> (D0 -> K- pi+) (pi0 -> gamma gamma) ) (rho(770)0 -> pi- pi+) ]cc}
#
from Configurables import Generation
Generation().EventType = 11164442
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dst0rho0,D0pi0,Kpi=DecProdCut,HELAMP100.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
