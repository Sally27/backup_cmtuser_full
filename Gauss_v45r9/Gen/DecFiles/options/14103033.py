# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/14103033.py generated: Fri, 27 Mar 2015 16:10:02
#
# Event Type: 14103033
#
# ASCII decay Descriptor: [B_c+ -> K+ K- K+]cc
#
from Configurables import Generation
Generation().EventType = 14103033
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_KKK=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
