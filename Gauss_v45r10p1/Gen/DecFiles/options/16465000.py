# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/16465000.py generated: Wed, 25 Jan 2017 15:25:14
#
# Event Type: 16465000
#
# ASCII decay Descriptor: [Sigma_b- -> Xi_b0 pi+]cc
#
from Configurables import Generation
Generation().EventType = 16465000
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xibst+_Xibpi=cocktail,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5112,-5112 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ " Sigma_b-   114   5112 -1.0  5.94550  6.000000e-020       Sigma_b-   5112  1.000000e-004", " Sigma_b~+  115  -5112  1.0  5.94550  6.000000e-020  anti-Sigma_b+  -5112  1.000000e-004" ]
