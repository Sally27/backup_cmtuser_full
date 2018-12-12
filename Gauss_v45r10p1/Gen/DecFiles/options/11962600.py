# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11962600.py generated: Wed, 25 Jan 2017 15:25:30
#
# Event Type: 11962600
#
# ASCII decay Descriptor: {[[B0]nos -> (D*(2010)~0 -> {(D~0 -> K+ pi-) pi0, (D~0 -> K+ pi-) gamma) X]cc, [[B0]os -> (D*(2010)0 -> {(D0 -> K- pi+) pi0, (D0 -> K- pi+) gamma) X]cc, [[B0]nos -> (D*(2010)0 -> {(D0 -> K- pi+) pi0, (D0 -> K- pi+) gamma}) X]cc, [[B0]os -> (D*(2010)~0 -> {(D~0 -> K+ pi-) pi0), (D~0 -> K+ pi-) gamma}) X]cc}
#
from Configurables import Generation
Generation().EventType = 11962600
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dst0X,Kpi.dec"
Generation().SignalRepeatedHadronization.CutTool = "LHCbAcceptance"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
