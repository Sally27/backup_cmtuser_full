# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/14143402.py generated: Fri, 27 Mar 2015 15:48:09
#
# Event Type: 14143402
#
# ASCII decay Descriptor: [B_c+ -> (J/psi(1S) -> mu+ mu- {,gamma} {,gamma}) (rho(770)+ -> pi+ (pi0 -> gamma gamma))]cc
#
from Configurables import Generation
Generation().EventType = 14143402
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_Jpsirho,mm=WeightedBcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
