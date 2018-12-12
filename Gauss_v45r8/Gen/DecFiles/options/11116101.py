# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11116101.py generated: Fri, 27 Mar 2015 15:48:11
#
# Event Type: 11116101
#
# ASCII decay Descriptor: [B0 -> (KS0 -> pi+ pi-) (A0 -> mu+ mu-)(Higgs'0 -> mu+ mu-)]cc
#
from Configurables import Generation
Generation().EventType = 11116101
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_KSPS,4mu=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "H_20  88  35  0.0  3.0     5.0e-12    Higgs'0   35    0.0" , "H_30  89  36  0.0  0.214   5.0e-12   A0   36    0.0" ]
