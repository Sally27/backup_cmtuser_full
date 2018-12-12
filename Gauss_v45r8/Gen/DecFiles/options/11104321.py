# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11104321.py generated: Fri, 27 Mar 2015 15:48:00
#
# Event Type: 11104321
#
# ASCII decay Descriptor: [B0 -> (phi -> K+ K-) (phi -> K+ K-) (K_S0 -> pi0 pi0)]cc
#
from Configurables import Generation
Generation().EventType = 11104321
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_phiphiKs,pi0pi0=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
