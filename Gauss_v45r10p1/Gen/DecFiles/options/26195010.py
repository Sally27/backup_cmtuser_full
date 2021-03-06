# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/26195010.py generated: Wed, 25 Jan 2017 15:25:16
#
# Event Type: 26195010
#
# ASCII decay Descriptor: [Sigma_c+ -> (Lambda_c+ -> p+ K- pi+) (D~0 -> K+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 26195010
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_X+_LcD0,pKpi,Kpi=phsp,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "Sigma_c+  83  4212  1.0  4.450 1.64553e-023      Sigma_c+   4212  0.00000000", "Sigma_c~- 84 -4212 -1.0  4.450 1.64553e-023 anti-Sigma_c-  -4212  0.00000000" ]

Generation().SignalPlain.SignalPIDList = [ 4212, -4212 ]

