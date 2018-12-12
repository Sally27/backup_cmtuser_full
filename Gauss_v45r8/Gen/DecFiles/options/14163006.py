# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/14163006.py generated: Fri, 27 Mar 2015 15:48:07
#
# Event Type: 14163006
#
# ASCII decay Descriptor: [B_c+ -> (D0 -> pi- pi+) pi+]cc
#
from Configurables import Generation
Generation().EventType = 14163006
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_D0pi+,pipi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
