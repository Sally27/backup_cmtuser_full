# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/14143012.py generated: Fri, 27 Mar 2015 15:48:04
#
# Event Type: 14143012
#
# ASCII decay Descriptor: [B_c+ -> (J/psi(1S) -> mu+ mu- {,gamma} {,gamma}) pi+]cc
#
from Configurables import Generation
Generation().EventType = 14143012
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_Jpsipi,mm=BcVegPy,NoCut.dec"
Generation().Special.CutTool = ""
