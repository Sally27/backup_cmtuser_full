# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11116001.py generated: Wed, 25 Jan 2017 15:25:33
#
# Event Type: 11116001
#
# ASCII decay Descriptor: [B0 -> (K*0 -> K+ pi-) (A0 -> mu+ mu-)(Higgs'0 -> mu+ mu-)]cc
#
from Configurables import Generation
Generation().EventType = 11116001
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_KstPS,4mu=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "H_20  88  35  0.0  1.0     5.0e-12    Higgs'0   35    0.0" , "H_30  89  36  0.0  0.214   5.0e-12   A0   36    0.0" ]
