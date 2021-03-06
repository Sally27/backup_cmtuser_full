# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/15196090.py generated: Fri, 27 Mar 2015 16:10:06
#
# Event Type: 15196090
#
# ASCII decay Descriptor: [Lambda_b0 -> (Sigma_c+ -> (Lambda_c+ -> p+ K- pi+) (D~0 -> K+ pi-)) K-]cc
#
from Configurables import Generation
Generation().EventType = 15196090
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_X+K-,LcD0,pKpi,Kpi=phsp,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "Sigma_c+  83  4212  1.0  4.450 1.64553e-023      Sigma_c+   4212  0.00000000", "Sigma_c~- 84 -4212 -1.0  4.450 1.64553e-023 anti-Sigma_c-  -4212  0.00000000" ]
