# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11198112.py generated: Fri, 27 Mar 2015 15:48:00
#
# Event Type: 11198112
#
# ASCII decay Descriptor: [B0 -> (D+ -> K- pi+ pi+) (D- -> K+ pi- pi-)  ( KS0 -> pi+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 11198112
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_DDKS,KPiPi,KPiPi,PiPi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
