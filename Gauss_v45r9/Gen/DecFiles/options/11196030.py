# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11196030.py generated: Fri, 27 Mar 2015 16:10:13
#
# Event Type: 11196030
#
# ASCII decay Descriptor: [B0 -> (D0 -> K- pi+) (D~0 -> K+ pi-) (K*0 -> K+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 11196030
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D0D0Kst0,KPi,KPi,KPi=sqDalitz,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
