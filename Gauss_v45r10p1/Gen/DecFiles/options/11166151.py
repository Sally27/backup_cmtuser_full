# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11166151.py generated: Wed, 25 Jan 2017 15:25:25
#
# Event Type: 11166151
#
# ASCII decay Descriptor: {[[B0]nos -> (D_s- => K+ K- pi-) (K*(892)+-> (K0S->pi+ pi-) pi+)]cc, [[B0]os -> (D_s+ => K- K+ pi+)  (K*(892)- -> (K0S->pi+ pi-) pi-)]cc}
#
from Configurables import Generation
Generation().EventType = 11166151
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_DsKst,KKpi,KSpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
