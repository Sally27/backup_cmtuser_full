# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/16165031.py generated: Fri, 27 Mar 2015 15:47:59
#
# Event Type: 16165031
#
# ASCII decay Descriptor: [Xi_b- -> (Lambda_c+ -> p K- pi+) pi- pi-]cc
#
from Configurables import Generation
Generation().EventType = 16165031
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xib_Lambdacpipi,pKpi=sqDalitz,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5132,-5132 ]
