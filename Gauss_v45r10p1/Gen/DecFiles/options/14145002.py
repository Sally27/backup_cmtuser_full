# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/14145002.py generated: Wed, 25 Jan 2017 15:25:25
#
# Event Type: 14145002
#
# ASCII decay Descriptor: [B_c+ -> (J/psi(1S) -> mu+ mu- {,gamma} {,gamma}) pi+ pi- pi+]cc
#
from Configurables import Generation
Generation().EventType = 14145002
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_Jpsipipipi,mm=WeightedBcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
