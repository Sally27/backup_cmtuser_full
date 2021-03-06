# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/16165231.py generated: Wed, 25 Jan 2017 15:25:24
#
# Event Type: 16165231
#
# ASCII decay Descriptor: [Xi_b- -> (Lambda_c+ -> p K- pi+)(a_1(1260)- -> pi- gamma) K- ]cc
#
from Configurables import Generation
Generation().EventType = 16165231
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xib_LambdacKa1,pKpi,pigamma=sqDalitz,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5132,-5132 ]
