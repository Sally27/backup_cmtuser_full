# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11164010.py generated: Wed, 25 Jan 2017 15:25:14
#
# Event Type: 11164010
#
# ASCII decay Descriptor: {[[B0]nos -> (D0 -> K- pi+) (K*(892)0 -> K+ pi-)]cc, [[B0]os -> (D~0 -> K+ pi-) (K*(892)~0 -> K- pi+)]cc}
#
from Configurables import Generation
Generation().EventType = 11164010
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D0Kst,Kpi=OS,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
