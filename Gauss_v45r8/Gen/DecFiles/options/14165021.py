# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/14165021.py generated: Fri, 27 Mar 2015 15:48:07
#
# Event Type: 14165021
#
# ASCII decay Descriptor: [B_c+ -> ([B+]nos -> (anti-D0 -> K+ pi-) pi+ ) K- pi+ ]cc
#
from Configurables import Generation
Generation().EventType = 14165021
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_BuK-pi+_D0pi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
