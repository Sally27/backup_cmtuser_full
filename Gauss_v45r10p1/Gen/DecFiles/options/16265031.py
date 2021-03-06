# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/16265031.py generated: Wed, 25 Jan 2017 15:25:15
#
# Event Type: 16265031
#
# ASCII decay Descriptor: [Xi_b- -> (Xi_c0 -> p K- K- pi+) pi-]cc
#
from Configurables import Generation
Generation().EventType = 16265031
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xib_Xic0pi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5132,-5132 ]
