# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11104080.py generated: Fri, 27 Mar 2015 15:48:11
#
# Event Type: 11104080
#
# ASCII decay Descriptor: [B0 -> (phi(1020) -> K+ K-) (phi(1020) -> K+ K-)]cc
#
from Configurables import Generation
Generation().EventType = 11104080
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_phiphi=CDFAmp,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
