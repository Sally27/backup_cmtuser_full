# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/14143201.py generated: Fri, 27 Mar 2015 15:48:02
#
# Event Type: 14143201
#
# ASCII decay Descriptor: [B_c+ -> ( chi_c1(1P) -> (J/psi(1S) -> mu+ mu- )  gamma ) pi+ ]cc
#
from Configurables import Generation
Generation().EventType = 14143201
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_chic1pi,mm=DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
