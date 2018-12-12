# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/18114014.py generated: Fri, 27 Mar 2015 16:10:10
#
# Event Type: 18114014
#
# ASCII decay Descriptor: Upsilon(2S) -> (Upsilon(1S) -> mu+ mu-) pi+ pi-
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Upsilon.py" )
from Configurables import Generation
Generation().EventType = 18114014
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xb_Upsilon1Spipi,mumu=DecProdCut,10.2GeV.dec"
Generation().Special.CutTool = "UpsilonDaughtersInLHCb"
from Configurables import UpsilonDaughtersInLHCb
Generation().Special.addTool( UpsilonDaughtersInLHCb )
Generation().Special.UpsilonDaughtersInLHCb.SignalPID = 100553
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ " Upsilon(2S)   831   100553  0.0  10.2  1.000000e-020       Upsilon(2S)   100553  1.000000e-004" ]
