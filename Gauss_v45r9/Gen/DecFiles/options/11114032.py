# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11114032.py generated: Fri, 27 Mar 2015 16:10:15
#
# Event Type: 11114032
#
# ASCII decay Descriptor: {[[B0]nos -> (Higgs0 -> mu+ mu-) (K*(892)0 -> K+ pi-)]cc, [[B0]os -> (Higgs0 -> mu- mu+) (K*(892)~0 -> K- pi+)]cc}
#
from Configurables import Generation
Generation().EventType = 11114032
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_KstInflaton2MuMu=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]

from Gauss.Configuration import *
from Configurables import LHCb__ParticlePropertySvc as ParticlePropertySvc
from Configurables import Gauss, PrintMCTree, PrintMCDecayTreeTool, HistogramPersistencySvc, NTupleSvc, DumpHepMCDecay, DumpHepMCTree, GaussMonitor__CheckLifeTimeHepMC, GaussMonitor__CheckLifeTimeMC, GiGa, GiGaPhysListModular, GiGaHiggsParticles, GenerationToSimulation, PythiaProduction



ParticlePropertySvc().Particles = [ "H_10     87      25  0.0        1.50   5.0000e-10      Higgs0   25   0.000000e+000" ]
ApplicationMgr().ExtSvc    += [ ParticlePropertySvc() ]




