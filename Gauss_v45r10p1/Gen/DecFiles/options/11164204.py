# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11164204.py generated: Wed, 25 Jan 2017 15:25:26
#
# Event Type: 11164204
#
# ASCII decay Descriptor: {[[B0]nos -> (D*(2007)~0 -> (D~0 -> K+ pi-) gamma ) pi- pi+ ]cc, [[B0]os -> (D*(2007)0 -> (D0 -> K- pi+) gamma ) pi+ pi- ]cc}
#
from Configurables import Generation
Generation().EventType = 11164204
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dst0pipi,D0gamma,Kpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
