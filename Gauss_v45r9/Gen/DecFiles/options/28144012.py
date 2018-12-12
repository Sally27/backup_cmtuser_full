# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/28144012.py generated: Fri, 27 Mar 2015 16:10:15
#
# Event Type: 28144012
#
# ASCII decay Descriptor: X_1(3872) -> (J/psi(1S) -> mu+ mu- {,gamma} {,gamma}) (rho(770)0 -> pi+ pi- {,gamma} {,gamma})
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/X3872_1PP.py" )
from Configurables import Generation
Generation().EventType = 28144012
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_X38721++,Jpsirho,mm=NoCut.dec"
Generation().Special.CutTool = ""
