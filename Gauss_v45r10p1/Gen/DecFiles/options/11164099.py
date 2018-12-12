# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11164099.py generated: Wed, 25 Jan 2017 15:25:35
#
# Event Type: 11164099
#
# ASCII decay Descriptor: {[[B0]nos -> (D_s- => K+ K- pi-) K+]cc, [[B0]os -> (D_s+ => K- K+ pi+) K-]cc}
#
from Configurables import Generation
Generation().EventType = 11164099
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Ds-K+,KKpi.dec"
Generation().SignalRepeatedHadronization.CutTool = ""
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
