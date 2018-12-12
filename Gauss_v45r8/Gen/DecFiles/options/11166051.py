# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11166051.py generated: Fri, 27 Mar 2015 15:48:06
#
# Event Type: 11166051
#
# ASCII decay Descriptor: {[[B0]nos => K+ K- (D~0 -> K+ pi- pi+ pi-)]cc, [[B0]os => K- K+ (D0 -> K- pi+ pi- pi+)]cc}
#
from Configurables import Generation
Generation().EventType = 11166051
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D0KK,K3pi=PHSP,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
