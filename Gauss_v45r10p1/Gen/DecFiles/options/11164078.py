# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11164078.py generated: Wed, 25 Jan 2017 15:25:27
#
# Event Type: 11164078
#
# ASCII decay Descriptor: {[[B0]nos => K+ pi- (D~0 -> K+ K-)]cc, [[B0]os => K- pi+ (D0 -> K- K+)]cc}
#
from Configurables import Generation
Generation().EventType = 11164078
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D0Kpi,KK=sqDalitz.dec"
Generation().SignalRepeatedHadronization.CutTool = ""
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
