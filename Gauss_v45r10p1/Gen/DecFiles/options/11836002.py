# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11836002.py generated: Wed, 25 Jan 2017 15:25:23
#
# Event Type: 11836002
#
# ASCII decay Descriptor: {[B0 -> (anti-D0 -> K+ pi-) pi- (tau+ -> pi+ pi+ pi- anti-nu_tau) nu_tau]cc,[B0 -> (anti-D*0 -> pi0 (anti-D0 -> K+ pi-)) pi- (tau+ -> pi+ pi+ pi- anti-nu_tau) nu_tau]cc,[B0 -> (anti-D*0 -> gamma (anti-D0 -> K+ pi-)) pi- (tau+ -> pi+ pi+ pi- anti-nu_tau) nu_tau]cc}
#
from Configurables import Generation
Generation().EventType = 11836002
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D0PiTauNu=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
