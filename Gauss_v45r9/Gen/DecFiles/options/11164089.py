# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11164089.py generated: Fri, 27 Mar 2015 16:10:08
#
# Event Type: 11164089
#
# ASCII decay Descriptor: {[[B0]nos => K+ K- (D~0 -> K+ K-)]cc, [[B0]os => K- K+ (D0 -> K- K+)]cc}
#
from Configurables import Generation
Generation().EventType = 11164089
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D0KK,KK=sqDalitz,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
