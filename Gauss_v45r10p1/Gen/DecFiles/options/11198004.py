# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11198004.py generated: Wed, 25 Jan 2017 15:25:29
#
# Event Type: 11198004
#
# ASCII decay Descriptor: [B0 -> D*(2010)- (D0 -> K- pi+ pi+ pi-) K+]cc
#
from Configurables import Generation
Generation().EventType = 11198004
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_DstD0K,D0pi_Kpi,K3pi=phsp,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
