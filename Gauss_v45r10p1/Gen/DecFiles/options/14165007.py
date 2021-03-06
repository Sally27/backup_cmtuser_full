# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/14165007.py generated: Wed, 25 Jan 2017 15:25:21
#
# Event Type: 14165007
#
# ASCII decay Descriptor: [B_c+ -> ([B0]nos -> (D- -> K+ pi- pi-) pi+, [B0]os -> (D+ -> K- pi+ pi+) pi-) K+]cc
#
from Configurables import Generation
Generation().EventType = 14165007
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_BdK+_Dpi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
