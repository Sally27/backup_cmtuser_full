# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/16165130.py generated: Fri, 27 Mar 2015 16:10:07
#
# Event Type: 16165130
#
# ASCII decay Descriptor: [Xi_b- -> (Sigma_c0 -> (Lambda_c+ -> Lambda0 pi+) pi-) K-]cc
#
from Configurables import Generation
Generation().EventType = 16165130
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xib_SigmacK,Lambdacpi,Lambdapi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5132,-5132 ]
