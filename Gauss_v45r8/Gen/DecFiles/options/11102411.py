# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11102411.py generated: Fri, 27 Mar 2015 15:48:00
#
# Event Type: 11102411
#
# ASCII decay Descriptor: [B0 -> (rho(770)+ -> pi+ (pi0 -> gamma gamma)) (rho(770)- -> pi- (pi0 -> gamma gamma))]cc
#
from Configurables import Generation
Generation().EventType = 11102411
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_rho+rho-=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
