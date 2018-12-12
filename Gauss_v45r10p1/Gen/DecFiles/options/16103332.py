# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/16103332.py generated: Wed, 25 Jan 2017 15:25:18
#
# Event Type: 16103332
#
# ASCII decay Descriptor: [Xi_b- -> (Omega- ->(Lambda0 -> p+ pi-) K- ) gamma]cc
#
from Configurables import Generation
Generation().EventType = 16103332
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Omegab_OmegaGamma=LHCbAcceptance.dec"
Generation().SignalRepeatedHadronization.CutTool = "LHCbAcceptance"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5132,-5132 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "Xi_b- 122 5132 -1.0 6.046 1.57e-012 Xi_b- 5132 0.000000e+000", "Xi_b~+ 123 -5132 1.0 6.046 1.57e-012 anti-Xi_b+ -5132 0.000000e+000" ]
