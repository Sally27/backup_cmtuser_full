# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/28144011.py generated: Fri, 27 Mar 2015 15:47:58
#
# Event Type: 28144011
#
# ASCII decay Descriptor: X_1(3872) -> (J/psi(1S) -> mu+ mu- {,gamma} {,gamma}) (rho(770)0 -> pi+ pi- {,gamma} {,gamma})
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/X3872_1PP.py" )
from Configurables import Generation
Generation().EventType = 28144011
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_X38721++,Jpsirho,mm=DecProdCut.dec"
Generation().Special.CutTool = "UpsilonDaughtersInLHCb"
from Configurables import UpsilonDaughtersInLHCb
Generation().Special.addTool( UpsilonDaughtersInLHCb )
Generation().Special.UpsilonDaughtersInLHCb.SignalPID = 9920443
