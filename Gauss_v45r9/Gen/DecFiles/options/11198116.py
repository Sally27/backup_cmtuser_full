# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11198116.py generated: Fri, 27 Mar 2015 16:10:00
#
# Event Type: 11198116
#
# ASCII decay Descriptor: [B0 -> (D- -> K+ pi- pi-) (D_s+ -> K+ K- pi+) (K_S0 -> pi+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 11198116
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_DsDKS,KKPi,KPiPi,PiPi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
