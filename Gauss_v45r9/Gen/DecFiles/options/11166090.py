# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11166090.py generated: Fri, 27 Mar 2015 16:10:11
#
# Event Type: 11166090
#
# ASCII decay Descriptor: [B0 -> (D- -> K- K+ pi-) K- K+ pi+]cc
#
from Configurables import Generation
Generation().EventType = 11166090
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D-KKpi,KKpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
