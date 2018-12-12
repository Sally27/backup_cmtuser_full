# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11696400.py generated: Wed, 25 Jan 2017 15:25:16
#
# Event Type: 11696400
#
# ASCII decay Descriptor: [B0-> (D- -> K+ pi- pi-)(D_s+ -> nu_tau (tau+ -> pi+ pi+ pi- pi0 anti-nu_tau))]cc
#
from Configurables import Generation
Generation().EventType = 11696400
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_DDs_TauNu,Tau2PiPiPiPi0Nu=DDalitz,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
