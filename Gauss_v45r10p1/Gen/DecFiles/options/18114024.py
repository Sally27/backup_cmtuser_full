# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/18114024.py generated: Wed, 25 Jan 2017 15:25:15
#
# Event Type: 18114024
#
# ASCII decay Descriptor: Upsilon(3S) -> (Upsilon(2S) -> mu+ mu-) pi+ pi-
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Upsilon.py" )
from Configurables import Generation
Generation().EventType = 18114024
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xb_Upsilon2Spipi,mumu=DecProdCut,10.6GeV.dec"
Generation().Special.CutTool = "UpsilonDaughtersInLHCb"
from Configurables import UpsilonDaughtersInLHCb
Generation().Special.addTool( UpsilonDaughtersInLHCb )
Generation().Special.UpsilonDaughtersInLHCb.SignalPID = 200553
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ " Upsilon(3S)   844   200553  0.0  10.6  1.000000e-020       Upsilon(3S)   200553  1.000000e-004" ]
