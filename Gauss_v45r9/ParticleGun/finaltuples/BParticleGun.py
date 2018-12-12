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
tsvc.EvtGenDecay.UserDecayFile = "Bu_Kstmumu.init.dec"
pgun.DecayTool = "EvtGenDecay"

pgun.MomentumRange.MomentumMin = 20.0*SystemOfUnits.GeV
pgun.MomentumRange.MomentumMax = 140.0*SystemOfUnits.GeV


from Gauss.Configuration import *
from Configurables import LHCb__ParticlePropertySvc as ParticlePropertySvc
from Configurables import Gauss, PrintMCTree, PrintMCDecayTreeTool, HistogramPersistencySvc, NTupleSvc, DumpHepMCDecay, DumpHepMCTree, GaussMonitor__CheckLifeTimeHepMC, GaussMonitor__CheckLifeTimeMC, GiGa, GiGaPhysListModular, GiGaHiggsParticles, GenerationToSimulation, PythiaProduction

#ParticlePropertySvc().Particles = [ "K*(892)+     38      323  1.0    0.891660   1.295693e-23     K*+   323   0.23", 
#                                    "K*(892)-     39     -323 -1.0    0.891660   1.295693e-23     K*-  -323   0.23"]
#ParticlePropertySvc().Particles = [ "K*(892)+     38      323  1.0    3.0    1.295693e-27      K*+   323   0.23", 
#                                    "K*(892)-     39     -323 -1.0    3.0    1.295693e-27     K*-  -323   0.23"]
#ApplicationMgr().ExtSvc    += [ ParticlePropertySvc() ]

ParticlePropertySvc().Particles = [ "K*(892)+     38      323  1.0    0.89166    1.295693e-26      K*+   323   2.085",
                                    "K*(892)-     39     -323 -1.0    0.89166    1.295693e-26     K*-  -323   2.085"]
ApplicationMgr().ExtSvc    += [ ParticlePropertySvc() ]


#gigaHiggsPart = GiGaHiggsParticles()
#gigaHiggsPart.Higgses = ["H_10"] # H_10, H_20, H_30
#GiGaPhysListModular("ModularPL").PhysicsConstructors += [ gigaHiggsPart ]#

#
