# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11104125.py generated: Fri, 27 Mar 2015 16:10:11
#
# Event Type: 11104125
#
# ASCII decay Descriptor: [B0 -> (eta_prime -> rho0 gamma) (Phi -> K+ K-)]cc
#
from Configurables import Generation
Generation().EventType = 11104125
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_etapPhi,rhogamma=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
