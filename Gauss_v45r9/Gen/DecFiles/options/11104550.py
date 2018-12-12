# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11104550.py generated: Fri, 27 Mar 2015 16:10:03
#
# Event Type: 11104550
#
# ASCII decay Descriptor: [B0 -> (K*0 -> (K_S0 -> pi+ pi-) (pi0 -> gamma gamma)) p+ anti-p-]cc
#
from Configurables import Generation
Generation().EventType = 11104550
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Kst0pp,KSpi0=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
