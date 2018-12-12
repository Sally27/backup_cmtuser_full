# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/16204042.py generated: Fri, 27 Mar 2015 15:48:05
#
# Event Type: 16204042
#
# ASCII decay Descriptor: [ Xi_b0 -> p+ K- K+ K- ]cc
#
from Configurables import Generation
Generation().EventType = 16204042
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xib0_pKKK=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5232,-5232 ]
