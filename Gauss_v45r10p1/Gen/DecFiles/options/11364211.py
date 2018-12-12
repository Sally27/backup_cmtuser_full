# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11364211.py generated: Wed, 25 Jan 2017 15:25:24
#
# Event Type: 11364211
#
# ASCII decay Descriptor: {[[B_s0]nos -> (D*_s- -> {gamma (D_s- => K+ K- pi-), pi0 (D_s- => K+ K- pi-)}) pi+]cc, [[B_s0]os -> (D*_s+ -> {gamma (D_s+ => K- K+ pi+), pi0 (D_s+ => K- K+ pi+)}) pi-]cc}
#
from Configurables import Generation
Generation().EventType = 11364211
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dsstpi,KKpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
