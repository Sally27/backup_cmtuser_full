# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/16303432.py generated: Wed, 25 Jan 2017 15:25:21
#
# Event Type: 16303432
#
# ASCII decay Descriptor: [Xi_b-  -> (N(1520)+ -> p+ pi0) K- K-]cc
#
from Configurables import Generation
Generation().EventType = 16303432
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xib_N+h-h-,p+pi0=phsp,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5132,-5132 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "N(1520)+ 122 2124 1.0 1.52 5.7217391e-024 N(1520)+ 2124 0.000000e+000", "N(1520)~- 123 -2124 -1.0 1.52 5.7217391e-024 anti-N(1520)- -2124 0.000000e+000" ]
