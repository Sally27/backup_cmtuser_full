# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11196042.py generated: Wed, 25 Jan 2017 15:25:20
#
# Event Type: 11196042
#
# ASCII decay Descriptor: [B0 -> (D+ -> K- pi+ pi+) (D~0 -> K+ pi-) pi-]cc
#
from Configurables import Generation
Generation().EventType = 11196042
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D0Dpi,KPi,KPiPi=sqDalitz23,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
