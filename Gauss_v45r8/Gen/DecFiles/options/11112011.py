# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11112011.py generated: Fri, 27 Mar 2015 15:48:05
#
# Event Type: 11112011
#
# ASCII decay Descriptor: {[B0 -> e- mu+]cc, [B0 -> e+ mu-]cc}
#
from Configurables import Generation
Generation().EventType = 11112011
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_emu=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
