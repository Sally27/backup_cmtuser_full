# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11264041.py generated: Fri, 27 Mar 2015 16:10:10
#
# Event Type: 11264041
#
# ASCII decay Descriptor: {[[B0]nos -> (D- => K+ K- pi-) K+]cc, [[B0]os -> (D+ => K- K+ pi+) K-]cc}
#
from Configurables import Generation
Generation().EventType = 11264041
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D-K+,KKpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
