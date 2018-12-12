# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11164131.py generated: Fri, 27 Mar 2015 15:48:13
#
# Event Type: 11164131
#
# ASCII decay Descriptor: {[[B0]nos -> (D~0 -> K+ K-) KS0]cc, [[B0]os -> (D0 -> K- K+) KS0]cc}
#
from Configurables import Generation
Generation().EventType = 11164131
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D0Ks,KK=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
