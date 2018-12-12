# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11164202.py generated: Fri, 27 Mar 2015 16:10:04
#
# Event Type: 11164202
#
# ASCII decay Descriptor: {[[B0]nos -> (D*(2007)~0 -> (D~0 -> K+ pi-) gamma ) (rho(770)0 -> pi+ pi-) ]cc, [[B0]os -> (D*(2007)0 -> (D0 -> K- pi+) gamma ) (rho(770)0 -> pi- pi+) ]cc}
#
from Configurables import Generation
Generation().EventType = 11164202
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dst0rho0,D0gamma,Kpi=DecProdCut,HELAMP010.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
