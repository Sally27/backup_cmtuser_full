# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11164082.py generated: Wed, 25 Jan 2017 15:25:30
#
# Event Type: 11164082
#
# ASCII decay Descriptor: {[[B0]nos => K+ K- (D~0 -> pi+ pi-)]cc, [[B0]os => K- K+ (D0 -> pi- pi+)]cc}
#
from Configurables import Generation
Generation().EventType = 11164082
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D0KK,pipi=PHSP.dec"
Generation().SignalRepeatedHadronization.CutTool = ""
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
