# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/17444263.py generated: Fri, 27 Mar 2015 15:48:05
#
# Event Type: 17444263
#
# ASCII decay Descriptor: [B*_20 ->  (B+ -> K+ (J/psi(1S) -> mu+ mu-)) pi-]cc, [B*_20 ->  (B+ -> (D~0 -> K+ pi-) pi+) pi-]cc, [B*_20 ->  ( B*+ -> (B+ -> K+ (J/psi(1S) -> mu+ mu- )) gamma ) pi-]cc, [B*_20 ->  ( B*+ -> (B+ -> (D~0 -> K+ pi-) pi+ ) gamma ) pi-]cc
#
from Configurables import Generation
Generation().EventType = 17444263
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bstst20_Bstpi,Bupi,JpsiK=DecProdCut,MaxMassDev750MeV.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 515,-515 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "B*_20    204  515    0.0  6.23000000  0.6582121e-024  B_2*0   515  0.750000", "B*_2~0    208    -515  0.0  6.23000000  0.6582121e-024  anti-B_2*0   -515  0.750000" ]
