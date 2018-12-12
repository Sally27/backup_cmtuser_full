# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/17144252.py generated: Wed, 25 Jan 2017 15:25:16
#
# Event Type: 17144252
#
# ASCII decay Descriptor: [B_s1(H)0 -> (B_s0 -> (J/psi(1S) -> mu+ mu- ) (phi(1020) -> K+ K-)) gamma]cc
#
from Configurables import Generation
Generation().EventType = 17144252
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bsprime1_Bsgamma,Jpsiphi,mm=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 10533,-10533 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "B_s1(L)0 211 10533 0.0 5.7660000 0.658000e-021 B_s10 10533 0.005000", "B_s1(L)~0 215 -10533 0.0 5.7660000 0.658000e-021 anti-B_s10 -10533 0.005000" ]
