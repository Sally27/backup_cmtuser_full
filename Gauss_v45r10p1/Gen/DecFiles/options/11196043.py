# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11196043.py generated: Wed, 25 Jan 2017 15:25:31
#
# Event Type: 11196043
#
# ASCII decay Descriptor: [B0 -> (D_s+ -> K+ K- pi+) (D~0 -> K+ pi-) pi-]cc
#
from Configurables import Generation
Generation().EventType = 11196043
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D0Dspi,KPi,KKPi=sqDalitz23,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
