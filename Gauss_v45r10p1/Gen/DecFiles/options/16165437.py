# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/16165437.py generated: Wed, 25 Jan 2017 15:25:35
#
# Event Type: 16165437
#
# ASCII decay Descriptor: [Xi_b- -> (Lambda_c+ -> p K- pi+)(rho(770)- -> pi- pi0) K-]cc
#
from Configurables import Generation
Generation().EventType = 16165437
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xib_LambdacrhoK,pKpi,pipi0=sqDalitz,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5132,-5132 ]
