# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/26104081.py generated: Wed, 25 Jan 2017 15:25:22
#
# Event Type: 26104081
#
# ASCII decay Descriptor: [Xi_c0 -> p+ K- K- pi+ ]cc
#
from Configurables import Generation
Generation().EventType = 26104081
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Omegac_pKKpi=phsp,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 4132,-4132 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "Xi_c0               106        4132  0.0        2.69520000      6.856377e-14            Xi_c0        4132   0.000", "Xi_c~0              107       -4132  0.0        2.69520000      6.856377e-14          anti-Xi_c0       -4132   0.000" ]
