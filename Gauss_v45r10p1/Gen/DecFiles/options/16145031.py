# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/16145031.py generated: Wed, 25 Jan 2017 15:25:27
#
# Event Type: 16145031
#
# ASCII decay Descriptor: [Xi_b- -> (J/psi(1S) -> mu+ mu-) K- pi+ anti-p-]cc
#
from Configurables import Generation
Generation().EventType = 16145031
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/X5750-_JpsiKpip,mumu=phsp,DecProdCut,PPChange.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5132,-5132 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "Xi_b-  122  5132  -1.0  5.750 1.5e-012      Xi_b-   5132  0.00000000", "Xi_b~+  123  -5132  1.0  5.750  1.5e-012 anti-Xi_b+  -5132  0.00000000" ]
