# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11114077.py generated: Fri, 27 Mar 2015 16:10:16
#
# Event Type: 11114077
#
# ASCII decay Descriptor: [B0 -> (K*(892)0 -> K+ pi-) (Higgs0 -> mu+ mu-)]cc
#
from Configurables import Generation
Generation().EventType = 11114077
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_KstarDarkBoson2MuMu,m=4000MeV,t=100ps,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]

from Gauss.Configuration import *
from Configurables import LHCb__ParticlePropertySvc as ParticlePropertySvc
from Configurables import Gauss, PrintMCTree, PrintMCDecayTreeTool, HistogramPersistencySvc, NTupleSvc, DumpHepMCDecay, DumpHepMCTree, GaussMonitor__CheckLifeTimeHepMC, GaussMonitor__CheckLifeTimeMC, GiGa, GiGaPhysListModular, GiGaHiggsParticles, GenerationToSimulation, PythiaProduction



ParticlePropertySvc().Particles = [ "H_10     87      25  0.0        4.0   1.0000e-10      Higgs0   25   0.000000e+000" ]
ApplicationMgr().ExtSvc    += [ ParticlePropertySvc() ]

gigaHiggsPart = GiGaHiggsParticles()
gigaHiggsPart.Higgses = ["H_10"] # H_10, H_20, H_30
GiGaPhysListModular("ModularPL").PhysicsConstructors += [ gigaHiggsPart ]#



