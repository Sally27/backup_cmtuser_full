# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11112401.py generated: Wed, 25 Jan 2017 15:25:31
#
# Event Type: 11112401
#
# ASCII decay Descriptor: [B0 -> mu+ mu- (pi0 -> gamma gamma)]cc
#
from Configurables import Generation
Generation().EventType = 11112401
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_pimumu=btosllball05,DiLeptonInAcc.dec"
Generation().SignalRepeatedHadronization.CutTool = ""
Generation().FullGenEventCutTool = "DiLeptonInAcceptance"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
