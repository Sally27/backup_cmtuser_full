# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11112410.py generated: Fri, 27 Mar 2015 15:48:03
#
# Event Type: 11112410
#
# ASCII decay Descriptor: [B0 -> (K_S0 -> pi0 pi0) mu+ mu-]cc
#
from Configurables import Generation
Generation().EventType = 11112410
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_KSmumu,pi0pi0=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
