# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/16464441.py generated: Fri, 27 Mar 2015 15:48:12
#
# Event Type: 16464441
#
# ASCII decay Descriptor: [Xi_b0 -> (D*(2010)~0 -> (D~0 -> K+ pi-) {pi0, gamma}) p+ K- ]cc
#
from Configurables import Generation
Generation().EventType = 16464441
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xib0_Dst0pK,Kpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5232,-5232 ]
