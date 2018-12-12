# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/16164041.py generated: Fri, 27 Mar 2015 15:47:58
#
# Event Type: 16164041
#
# ASCII decay Descriptor: [Xi_b0 -> (D0 -> K- pi+) p+ K- ]cc
#
from Configurables import Generation
Generation().EventType = 16164041
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xib0_D0pK,Kpi=DecProdCut,fix.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5232,-5232 ]
