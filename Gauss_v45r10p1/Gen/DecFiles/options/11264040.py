# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11264040.py generated: Wed, 25 Jan 2017 15:25:23
#
# Event Type: 11264040
#
# ASCII decay Descriptor: {[[B0]nos -> (D- => K+ K- pi-) K+]cc, [[B0]os -> (D+ => K- K+ pi+) K-]cc}
#
from Configurables import Generation
Generation().EventType = 11264040
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D-K+,KKpi.dec"
Generation().SignalRepeatedHadronization.CutTool = ""
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
