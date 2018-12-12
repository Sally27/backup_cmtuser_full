# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/18212263.py generated: Fri, 27 Mar 2015 16:10:03
#
# Event Type: 18212263
#
# ASCII decay Descriptor: chi_b1(3P) -> (Upsilon -> mu+ mu-) gamma
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Upsilon.py" )
from Configurables import Generation
Generation().EventType = 18212263
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_chib13P,Upsilongamma,mumu=UpsInAcc.dec"
Generation().Special.CutTool = "UpsilonDaughtersInLHCb"
from Configurables import UpsilonDaughtersInLHCb
Generation().Special.addTool( UpsilonDaughtersInLHCb )
Generation().Special.UpsilonDaughtersInLHCb.NeutralThetaMin = 0.
Generation().Special.UpsilonDaughtersInLHCb.NeutralThetaMax = 10.
Generation().Special.UpsilonDaughtersInLHCb.SignalPID = 20553
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "chi_b1(1P) 695 20553 0.0 10.516 0.000000e+000 chi_b1 20553 0.000000e+000" ]
