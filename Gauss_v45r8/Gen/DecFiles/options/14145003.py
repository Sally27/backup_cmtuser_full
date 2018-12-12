# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/14145003.py generated: Fri, 27 Mar 2015 15:47:57
#
# Event Type: 14145003
#
# ASCII decay Descriptor: [B_c+ -> [B_s0 -> (J/psi(1S) -> mu+ mu- {,gamma} {,gamma}) (phi(1020) -> K+ K-)]cc, pi+]cc
#
from Configurables import Generation
Generation().EventType = 14145003
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_Bspi,Jpsiphi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
