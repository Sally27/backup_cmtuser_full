# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11198126.py generated: Wed, 25 Jan 2017 15:25:26
#
# Event Type: 11198126
#
# ASCII decay Descriptor: [B0 -> (D- -> K+ pi- pi-) (D_s+ -> K+ K- pi+) (K_S0 -> pi+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 11198126
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_DsDKS,KKPi,KPiPi,PiPi=sqDalitz,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
