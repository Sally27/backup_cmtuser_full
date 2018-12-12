# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/16265033.py generated: Fri, 27 Mar 2015 16:10:08
#
# Event Type: 16265033
#
# ASCII decay Descriptor: [Xi_b- -> (Lambda_b -> (Lambda_c+ -> p K- pi+) pi-) pi-]cc
#
from Configurables import Generation
Generation().EventType = 16265033
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xib_Lbpi,pKpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5132,-5132 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ " Xi_b-   122   5132  -1.0  5.7977  1.600000e-012       Xi_b-   5132  0.000000e+000", " Xi_b~+  123  -5132  1.0  5.7977  1.600000e-012  anti-Xi_b+  -5132  0.000000e+000" ]
