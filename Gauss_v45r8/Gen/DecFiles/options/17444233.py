# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/17444233.py generated: Fri, 27 Mar 2015 15:48:07
#
# Event Type: 17444233
#
# ASCII decay Descriptor: [B_1(L)0 ->  ( B*+ -> (B+ -> K+ (J/psi(1S) -> mu+ mu- )) gamma ) K-]cc, [B_1(L)0 ->  ( B*+ -> (B+ -> (D~0 -> K+ pi-) pi+ ) gamma ) K-]cc
#
from Configurables import Generation
Generation().EventType = 17444233
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bstst10_Bstpi,JpsiK=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 10513,-10513 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "B_1(L)0  203  10513  0.0  6.23000000  0.6582121e-024  B_10  10513  0.750000", "B_1(L)~0  207  -10513  0.0  6.23000000  0.6582121e-024  anti-B_10  -10513  0.750000" ]
