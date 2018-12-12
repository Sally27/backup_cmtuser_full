# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/14103053.py generated: Fri, 27 Mar 2015 16:10:12
#
# Event Type: 14103053
#
# ASCII decay Descriptor: [B_c+ -> (B0 -> pi+ pi-) K+]cc
#
from Configurables import Generation
Generation().EventType = 14103053
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_BdK+,CPVpipi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
