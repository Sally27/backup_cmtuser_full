# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/18112271.py generated: Wed, 25 Jan 2017 15:25:26
#
# Event Type: 18112271
#
# ASCII decay Descriptor: chi_b2(1P) -> (Upsilon -> mu+ mu-) gamma
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Upsilon.py" )
from Configurables import Generation
Generation().EventType = 18112271
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_chib21P,Upsilongamma,mumu=UpsInAcc.dec"
Generation().Special.CutTool = "UpsilonDaughtersInLHCb"
from Configurables import UpsilonDaughtersInLHCb
Generation().Special.addTool( UpsilonDaughtersInLHCb )
Generation().Special.UpsilonDaughtersInLHCb.NeutralThetaMin = 0.
Generation().Special.UpsilonDaughtersInLHCb.NeutralThetaMax = 10.
Generation().Special.UpsilonDaughtersInLHCb.SignalPID = 555
