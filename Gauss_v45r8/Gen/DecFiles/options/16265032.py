# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/16265032.py generated: Fri, 27 Mar 2015 15:47:58
#
# Event Type: 16265032
#
# ASCII decay Descriptor: [Xi_b- -> (Xi_c0 -> p K- K- pi+) K-]cc
#
from Configurables import Generation
Generation().EventType = 16265032
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xib_Xic0K=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5132,-5132 ]
