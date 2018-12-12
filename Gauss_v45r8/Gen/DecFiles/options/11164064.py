# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11164064.py generated: Fri, 27 Mar 2015 15:48:00
#
# Event Type: 11164064
#
# ASCII decay Descriptor: {[[B0]nos => pi+ pi- (D~0 -> K+ K-)]cc, [[B0]os => pi- pi+ (D0 -> K- K+)]cc}
#
from Configurables import Generation
Generation().EventType = 11164064
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D0pipi,KK=PHSP.dec"
Generation().SignalRepeatedHadronization.CutTool = ""
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
