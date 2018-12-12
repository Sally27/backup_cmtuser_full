# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11566420.py generated: Wed, 25 Jan 2017 15:25:27
#
# Event Type: 11566420
#
# ASCII decay Descriptor: [B0 -> (D*- -> pi- (anti-D0 -> K+ pi-)) (tau+ -> pi+ pi+ pi- pi0 anti-nu_tau) nu_tau]cc
#
from Configurables import Generation
Generation().EventType = 11566420
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_DstTauNu,Tau2PiPiPiPi0Nu,pi0notreqinacc=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
from Configurables import DaughtersInLHCb
Generation().SignalRepeatedHadronization.addTool( DaughtersInLHCb )
Generation().SignalRepeatedHadronization.DaughtersInLHCb.NeutralThetaMin = 0.
Generation().SignalRepeatedHadronization.DaughtersInLHCb.NeutralThetaMax = 10.
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
