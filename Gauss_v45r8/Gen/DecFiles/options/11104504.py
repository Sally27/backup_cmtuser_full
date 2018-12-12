# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11104504.py generated: Fri, 27 Mar 2015 15:47:59
#
# Event Type: 11104504
#
# ASCII decay Descriptor: [B0 -> (K*0 -> (K_S0 -> pi+ pi-) (pi0 -> gamma gamma)) pi+ pi-]cc
#
from Configurables import Generation
Generation().EventType = 11104504
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Kst0pipi,KSpi0=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]