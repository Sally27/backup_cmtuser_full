# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/18244001.py generated: Fri, 27 Mar 2015 15:48:05
#
# Event Type: 18244001
#
# ASCII decay Descriptor: Upsilon(1S) -> [ (B_c+ -> (J/psi(1S) -> mu+ mu- {,gamma} {,gamma}) pi+ {,gamma} {,gamma} ) ]cc pi- {,gamma} {,gamma}
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Upsilon.py" )
from Configurables import Generation
Generation().EventType = 18244001
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Upsilon_Bcpi,Jpsipi,mm=DecProdCut.dec"
Generation().Special.CutTool = "UpsilonDaughtersInLHCb"
from Configurables import UpsilonDaughtersInLHCb
Generation().Special.addTool( UpsilonDaughtersInLHCb )
Generation().Special.UpsilonDaughtersInLHCb.SignalPID = 553
