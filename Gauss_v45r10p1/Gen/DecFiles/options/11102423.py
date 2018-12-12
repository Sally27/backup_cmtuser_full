# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11102423.py generated: Wed, 25 Jan 2017 15:25:17
#
# Event Type: 11102423
#
# ASCII decay Descriptor: {[[B0]nos -> K+ K- (pi0 -> gamma gamma)]cc, [[B0]os -> K- K+ (pi0 -> gamma gamma)]cc}
#
from Configurables import Generation
Generation().EventType = 11102423
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_K+K-pi0=sqDalitz.dec"
Generation().SignalRepeatedHadronization.CutTool = "LHCbAcceptance"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
