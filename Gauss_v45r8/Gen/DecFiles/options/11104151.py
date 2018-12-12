# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11104151.py generated: Fri, 27 Mar 2015 15:48:04
#
# Event Type: 11104151
#
# ASCII decay Descriptor: {[B0 -> (K*(892)~0 -> K- pi+) (KS0 -> pi+ pi-)]cc, [B0 -> (K*(892)0 -> K+ pi-) (K_S0 -> pi+ pi-)]cc}
#
from Configurables import Generation
Generation().EventType = 11104151
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_KstKS=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
