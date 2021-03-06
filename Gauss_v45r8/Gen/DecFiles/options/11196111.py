# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11196111.py generated: Fri, 27 Mar 2015 15:48:09
#
# Event Type: 11196111
#
# ASCII decay Descriptor: [B0 -> (D0 -> K- pi+) (D~0 -> K+ pi-) ( KS0 -> pi+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 11196111
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D0D0KS,KPi,KPi,PiPi=sqDalitz,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
