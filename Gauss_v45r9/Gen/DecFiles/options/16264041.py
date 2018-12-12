# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/16264041.py generated: Fri, 27 Mar 2015 16:10:03
#
# Event Type: 16264041
#
# ASCII decay Descriptor: [Xi_b0 -> (Xi_c+ -> p K+ pi-) pi-]cc
#
from Configurables import Generation
Generation().EventType = 16264041
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xib0_Xicpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5232,-5232 ]
