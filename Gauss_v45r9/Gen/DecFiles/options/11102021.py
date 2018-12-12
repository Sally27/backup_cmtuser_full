# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11102021.py generated: Fri, 27 Mar 2015 16:10:17
#
# Event Type: 11102021
#
# ASCII decay Descriptor: [B0 -> K+ K-]cc
#
from Configurables import Generation
Generation().EventType = 11102021
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_K+K-=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]