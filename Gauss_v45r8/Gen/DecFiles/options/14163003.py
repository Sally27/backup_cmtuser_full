# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/14163003.py generated: Fri, 27 Mar 2015 15:48:11
#
# Event Type: 14163003
#
# ASCII decay Descriptor: [B_c+ -> (D0 -> K- K+) K+]cc
#
from Configurables import Generation
Generation().EventType = 14163003
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_D0K+,KK=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
