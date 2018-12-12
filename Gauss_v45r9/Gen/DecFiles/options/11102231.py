# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11102231.py generated: Fri, 27 Mar 2015 16:10:18
#
# Event Type: 11102231
#
# ASCII decay Descriptor: [B0 -> (phi(1020) -> K+ K-) gamma]cc
#
from Configurables import Generation
Generation().EventType = 11102231
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_phigamma,KK=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
