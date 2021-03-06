# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11166161.py generated: Fri, 27 Mar 2015 15:48:10
#
# Event Type: 11166161
#
# ASCII decay Descriptor: {[[B0]nos => (K_S0 -> pi+ pi-) (D- => K+ pi- pi-) pi+]cc, [[B0]os => (K_S0 -> pi+ pi-) (D+ => K- pi+ pi+) pi-]cc}
#
from Configurables import Generation
Generation().EventType = 11166161
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D-KSpi,Kpipi=sqDalitz,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
