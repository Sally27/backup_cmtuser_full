# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/18114013.py generated: Fri, 27 Mar 2015 16:10:08
#
# Event Type: 18114013
#
# ASCII decay Descriptor: Upsilon(4S) -> (Upsilon(1S) -> mu+ mu- {,gamma} {,gamma}) K+ K-
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Upsilon.py" )
from Configurables import Generation
Generation().EventType = 18114013
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_Upsilon4S,Upsilon1SKK=DecProdCut,fix.dec"
Generation().Special.CutTool = "UpsilonDaughtersInLHCb"
from Configurables import UpsilonDaughtersInLHCb
Generation().Special.addTool( UpsilonDaughtersInLHCb )
Generation().Special.UpsilonDaughtersInLHCb.SignalPID = 100553
