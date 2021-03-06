# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/16165435.py generated: Wed, 25 Jan 2017 15:25:28
#
# Event Type: 16165435
#
# ASCII decay Descriptor: [Xi_b- -> (Sigma_c(2455)+ -> pi0 (Lambda_c+ -> p K- pi+)) K- K-]cc
#
from Configurables import Generation
Generation().EventType = 16165435
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xib_SigmacKK,Lambdacpi0,pKpi=sqDalitz,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5132,-5132 ]
