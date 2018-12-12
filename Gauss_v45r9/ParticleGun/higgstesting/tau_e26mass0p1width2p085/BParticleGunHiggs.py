# content of the file BParticleGun.py
from Configurables import ParticleGun, MomentumRange, FlatNParticles, ToolSvc, EvtGenDecay
from GaudiKernel import SystemOfUnits

pgun = ParticleGun()
pgun.ParticleGunTool = "MomentumRange"
pgun.addTool(MomentumRange, name = "MomentumRange")

pgun.NumberOfParticlesTool = "FlatNParticles"
pgun.addTool(FlatNParticles, name = "FlatNParticles")

pgun.MomentumRange.PdgCodes = [521, -521]

tsvc = ToolSvc()
tsvc.addTool(EvtGenDecay, name = "EvtGenDecay")
tsvc.EvtGenDecay.UserDecayFile = "BuHiggs.dec"
pgun.DecayTool = "EvtGenDecay"

pgun.MomentumRange.MomentumMin = 20.0*SystemOfUnits.GeV
pgun.MomentumRange.MomentumMax = 140.0*SystemOfUnits.GeV


from Gauss.Configuration import *
from Configurables import LHCb__ParticlePropertySvc as ParticlePropertySvc
from Configurables import Gauss, PrintMCTree, PrintMCDecayTreeTool, HistogramPersistencySvc, NTupleSvc, DumpHepMCDecay, DumpHepMCTree, GaussMonitor__CheckLifeTimeHepMC, GaussMonitor__CheckLifeTimeMC, GiGa, GiGaPhysListModular, GiGaHiggsParticles, GenerationToSimulation, PythiaProduction


ParticlePropertySvc().Particles = ["H_10     87  25  1.0  0.1    1.295693e-26      Higgs0   25   2.085",
                                   "H_20     88  35  -1.0  0.1    1.295693e-26      Higgs'0   35   2.085"]


ApplicationMgr().ExtSvc    += [ ParticlePropertySvc() ]
gigaHiggsPart = GiGaHiggsParticles()
gigaHiggsPart.Higgses = ["H_10","H_20"]
GiGaPhysListModular("ModularPL").PhysicsConstructors += [ gigaHiggsPart ]
