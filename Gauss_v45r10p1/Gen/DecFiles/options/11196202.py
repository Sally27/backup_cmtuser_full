# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11196202.py generated: Wed, 25 Jan 2017 15:25:17
#
# Event Type: 11196202
#
# ASCII decay Descriptor: [B0 -> K+ (D*- -> (anti-D0 -> K+ pi-) pi-) (D*0 -> (D0 -> K- pi+) gamma)]cc
#
from Configurables import Generation
Generation().EventType = 11196202
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dst0DstK,D0gamma,Kpi,PHSP=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
