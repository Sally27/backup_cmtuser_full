# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/16264042.py generated: Fri, 27 Mar 2015 15:47:57
#
# Event Type: 16264042
#
# ASCII decay Descriptor: [Xi_b0 -> (Xi_c+ -> p K+ pi-) K-]cc
#
from Configurables import Generation
Generation().EventType = 16264042
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xib0_XicK=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5232,-5232 ]
