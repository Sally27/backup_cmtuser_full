# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/17146052.py generated: Wed, 25 Jan 2017 15:25:24
#
# Event Type: 17146052
#
# ASCII decay Descriptor: [B_s1(L)0 -> (B_s0 -> (J/psi(1S) -> mu+ mu- ) (phi(1020) -> K+ K-) ) pi+ pi-]cc
#
from Configurables import Generation
Generation().EventType = 17146052
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bs1_Bspipi,Jpsiphi,mm=DDalitz,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 10533,-10533 ]
