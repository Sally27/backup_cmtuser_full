# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11114074.py generated: Wed, 25 Jan 2017 15:25:19
#
# Event Type: 11114074
#
# ASCII decay Descriptor: [B0 -> (K*(892)0 -> K+ pi-) (Higgs0 -> mu+ mu-)]cc
#
from Configurables import Generation
Generation().EventType = 11114074
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_KstarDarkBoson2MuMu,m=250MeV,t=100ps,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]

from Gauss.Configuration import *
from Configurables import LHCb__ParticlePropertySvc as ParticlePropertySvc
from Configurables import Gauss, PrintMCTree, PrintMCDecayTreeTool, HistogramPersistencySvc, NTupleSvc, DumpHepMCDecay, DumpHepMCTree, GaussMonitor__CheckLifeTimeHepMC, GaussMonitor__CheckLifeTimeMC, GiGa, GiGaPhysListModular, GiGaHiggsParticles, GenerationToSimulation, PythiaProduction



ParticlePropertySvc().Particles = [ "H_10     87      25  0.0        0.250   1.0000e-10      Higgs0   25   0.000000e+000" ]
ApplicationMgr().ExtSvc    += [ ParticlePropertySvc() ]

gigaHiggsPart = GiGaHiggsParticles()
gigaHiggsPart.Higgses = ["H_10"] # H_10, H_20, H_30
GiGaPhysListModular("ModularPL").PhysicsConstructors += [ gigaHiggsPart ]#



