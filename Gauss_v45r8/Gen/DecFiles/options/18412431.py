# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/18412431.py generated: Fri, 27 Mar 2015 15:48:06
#
# Event Type: 18412431
#
# ASCII decay Descriptor: Upsilon(4S) -> (Upsilon(1S) -> mu+ mu- {,gamma} {,gamma}) (eta -> pi+ pi- pi0)
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Upsilon.py" )
from Configurables import Generation
Generation().EventType = 18412431
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_Upsilon4S,Upsilon1Seta=Pwave,DecProdCut,fix.dec"
Generation().Special.CutTool = "UpsilonDaughtersInLHCb"
from Configurables import UpsilonDaughtersInLHCb
Generation().Special.addTool( UpsilonDaughtersInLHCb )
Generation().Special.UpsilonDaughtersInLHCb.SignalPID = 300553
