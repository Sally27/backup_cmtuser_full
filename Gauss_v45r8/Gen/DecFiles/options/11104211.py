# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11104211.py generated: Fri, 27 Mar 2015 15:47:57
#
# Event Type: 11104211
#
# ASCII decay Descriptor: [B0 -> (phi(1020) -> K+ K-) (phi(1020) -> K+ K-)  gamma]cc
#
from Configurables import Generation
Generation().EventType = 11104211
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_phiphigamma,KKKK=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
