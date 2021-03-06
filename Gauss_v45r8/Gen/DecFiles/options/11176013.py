# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11176013.py generated: Fri, 27 Mar 2015 15:48:12
#
# Event Type: 11176013
#
# ASCII decay Descriptor: [B0 -> (D*(2010)- -> pi- (D~0 -> K+ pi-)) mu+ (N-> mu+ pi-) {,gamma}{,gamma}]cc
#
from Configurables import Generation
Generation().EventType = 11176013
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dstmumupi,mN=2000MeV=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "N 1235 19 0.0 2.0 0 N 19 0.0","anti-N 1236 -19 0.0 2.0 0 anti-N -19 0.0" ]
