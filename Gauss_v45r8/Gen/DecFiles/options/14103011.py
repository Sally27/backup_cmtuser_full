# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/14103011.py generated: Fri, 27 Mar 2015 15:47:57
#
# Event Type: 14103011
#
# ASCII decay Descriptor: [B_c+ -> (phi(1020) -> K+ K-) K+]cc
#
from Configurables import Generation
Generation().EventType = 14103011
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_phiK=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
