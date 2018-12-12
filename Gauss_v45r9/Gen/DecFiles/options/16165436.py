# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/16165436.py generated: Fri, 27 Mar 2015 16:10:15
#
# Event Type: 16165436
#
# ASCII decay Descriptor: [Xi_b- -> (Lambda_c+ -> p K- pi+)(K*(892)- -> K- pi0) K-]cc
#
from Configurables import Generation
Generation().EventType = 16165436
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xib_LambdacKstK,pKpi,Kpi0=sqDalitz,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5132,-5132 ]
