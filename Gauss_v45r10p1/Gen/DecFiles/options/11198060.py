# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11198060.py generated: Wed, 25 Jan 2017 15:25:17
#
# Event Type: 11198060
#
# ASCII decay Descriptor: [B0 -> (D*(2010)- -> (anti-D0 -> K+ pi+ pi- pi-) pi-) (D_s+ -> K- K+ pi+ ) ]cc
#
from Configurables import Generation
Generation().EventType = 11198060
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_DstDs,D0K3pi,DsKpipi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
