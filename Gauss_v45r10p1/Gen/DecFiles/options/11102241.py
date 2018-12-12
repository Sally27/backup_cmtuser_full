# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11102241.py generated: Wed, 25 Jan 2017 15:25:32
#
# Event Type: 11102241
#
# ASCII decay Descriptor: {[ [B0]nos ->  (K*_2(1430)0 ->  K+ pi-) gamma ]cc , [[B0]os -> (K*_2(1430)~0 ->  K- pi+) gamma]cc}
#
from Configurables import Generation
Generation().EventType = 11102241
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_K2st0gamma,Kpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
