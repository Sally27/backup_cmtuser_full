# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11166080.py generated: Fri, 27 Mar 2015 15:48:14
#
# Event Type: 11166080
#
# ASCII decay Descriptor: [B0 -> (D- -> K- K+ pi-) anti-p- p+ pi+]cc
#
from Configurables import Generation
Generation().EventType = 11166080
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D-ppbarpi,KKpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
