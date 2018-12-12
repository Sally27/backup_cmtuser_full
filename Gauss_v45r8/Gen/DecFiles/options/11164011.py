# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11164011.py generated: Fri, 27 Mar 2015 15:48:01
#
# Event Type: 11164011
#
# ASCII decay Descriptor: {[[B0]nos -> (D~0 -> K+ pi-) (K*(892)0 -> K+ pi-)]cc, [[B0]os -> (D0 -> K- pi+) (K*(892)~0 -> K- pi+)]cc}
#
from Configurables import Generation
Generation().EventType = 11164011
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D0Kst,Kpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
