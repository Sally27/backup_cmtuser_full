# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11196201.py generated: Wed, 25 Jan 2017 15:25:22
#
# Event Type: 11196201
#
# ASCII decay Descriptor: [B0 -> K+ (D*0 -> (D0 -> K- pi+) gamma) (anti-D0 -> K+ pi-) pi-]cc
#
from Configurables import Generation
Generation().EventType = 11196201
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dst0D0Kpi,D0gamma,Kpi=PHSP,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
