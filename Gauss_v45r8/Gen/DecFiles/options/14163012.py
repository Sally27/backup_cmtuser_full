# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/14163012.py generated: Fri, 27 Mar 2015 15:47:59
#
# Event Type: 14163012
#
# ASCII decay Descriptor: [B_c+ -> (D0 -> K- pi+) K+]cc
#
from Configurables import Generation
Generation().EventType = 14163012
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_D0K,Kpi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
