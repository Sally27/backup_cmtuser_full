# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/16165033.py generated: Fri, 27 Mar 2015 16:10:00
#
# Event Type: 16165033
#
# ASCII decay Descriptor: [Xi_b- -> (Lambda_c+ -> p K- pi+) K- K-]cc
#
from Configurables import Generation
Generation().EventType = 16165033
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xib_LambdacKK,pKpi=sqDalitz,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5132,-5132 ]
