# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/16165036.py generated: Fri, 27 Mar 2015 15:48:13
#
# Event Type: 16165036
#
# ASCII decay Descriptor: [Xi_b- -> (Lambda_c+ -> p K- pi+) K- K-]cc
#
from Configurables import Generation
Generation().EventType = 16165036
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Omegab_LambdacKK,pKpi=sqDalitz,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5132,-5132 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "Xi_b- 122 5132 -1.0 6.071 1.1e-012 Xi_b- 5132 0.000000e+000", "Xi_b~+ 123 -5132 1.0 6.071 1.1e-012 anti-Xi_b+ -5132 0.000000e+000" ]
