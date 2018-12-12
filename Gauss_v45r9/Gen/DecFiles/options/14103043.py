# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/14103043.py generated: Fri, 27 Mar 2015 16:10:07
#
# Event Type: 14103043
#
# ASCII decay Descriptor: [B_c+ -> (B_s0 -> K+ K-) K+]cc
#
from Configurables import Generation
Generation().EventType = 14103043
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_BsK+,KK=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
