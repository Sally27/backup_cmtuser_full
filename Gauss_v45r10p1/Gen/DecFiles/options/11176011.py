# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11176011.py generated: Wed, 25 Jan 2017 15:25:28
#
# Event Type: 11176011
#
# ASCII decay Descriptor: [B0 -> (D*(2010)- -> pi- (D~0 -> K+ pi-)) mu+ (N-> mu+ pi-) {,gamma}{,gamma}]cc
#
from Configurables import Generation
Generation().EventType = 11176011
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dstmumupi,mN=260MeV=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "N 1235 19 0.0 0.26 0 N 19 0.0","anti-N 1236 -19 0.0 0.26 0 anti-N -19 0.0" ]
