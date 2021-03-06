# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11114044.py generated: Wed, 25 Jan 2017 15:25:17
#
# Event Type: 11114044
#
# ASCII decay Descriptor: { B0 -> (Higgs0 -> mu+ pi-) mu+ pi-, B~0 -> (Higgs0 -> mu- pi+) mu- pi+ }
#
from Configurables import Generation
Generation().EventType = 11114044
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_MuPiMajoranaNeutrino2MuPi,m=1500MeV,t=10ps,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]

from Gauss.Configuration import *
from Configurables import LHCb__ParticlePropertySvc as ParticlePropertySvc
from Configurables import Gauss, PrintMCTree, PrintMCDecayTreeTool, HistogramPersistencySvc, NTupleSvc, DumpHepMCDecay, DumpHepMCTree, GaussMonitor__CheckLifeTimeHepMC, GaussMonitor__CheckLifeTimeMC, GiGa, GiGaPhysListModular, GiGaHiggsParticles, GenerationToSimulation, PythiaProduction

ParticlePropertySvc().Particles = [ "H_10 87 25 0.0000 1.5000 1.0000e-11 Higgs0 25 0.0000" ]
ApplicationMgr().ExtSvc += [ ParticlePropertySvc() ]

gigaHiggsPart = GiGaHiggsParticles()
gigaHiggsPart.Higgses = ["H_10"]
GiGaPhysListModular("ModularPL").PhysicsConstructors += [ gigaHiggsPart ]

