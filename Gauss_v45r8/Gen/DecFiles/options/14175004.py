# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/14175004.py generated: Fri, 27 Mar 2015 15:47:57
#
# Event Type: 14175004
#
# ASCII decay Descriptor: [B_c+ -> (D_s+ -> K+ K- pi+) mu+ mu-]cc
#
from Configurables import Generation
Generation().EventType = 14175004
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_Dsmumu=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
