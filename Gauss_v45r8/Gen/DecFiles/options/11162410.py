# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11162410.py generated: Fri, 27 Mar 2015 15:48:09
#
# Event Type: 11162410
#
# ASCII decay Descriptor: [B0 -> (anti-D0 -> K+ K-) (pi0 -> gamma gamma)]cc
#
from Configurables import Generation
Generation().EventType = 11162410
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D0pi0,KK=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
