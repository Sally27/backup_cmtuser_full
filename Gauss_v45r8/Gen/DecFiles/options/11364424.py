# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11364424.py generated: Fri, 27 Mar 2015 15:48:14
#
# Event Type: 11364424
#
# ASCII decay Descriptor: {[[B0]nos -> (D*(2007)~0 -> {(D~0 -> pi+ pi-) (pi0 -> gamma gamma), (D~0 -> pi+ pi-) gamma} ) K+ pi- ]cc, [[B0]os -> (D*(2007)0 -> {(D0 -> pi- pi+) (pi0 -> gamma gamma), (D0 -> pi- pi+) gamma} ) K- pi+ ]cc}
#
from Configurables import Generation
Generation().EventType = 11364424
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dst0Kpi,D0,pipi=sqDalitz,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
