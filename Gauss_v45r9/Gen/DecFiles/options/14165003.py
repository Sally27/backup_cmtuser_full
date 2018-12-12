# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/14165003.py generated: Fri, 27 Mar 2015 16:10:14
#
# Event Type: 14165003
#
# ASCII decay Descriptor: [B_c+ -> ([B_s0]nos -> (D_s- -> K+ K- pi-) pi+, [B_s0]os -> (D_s+ -> K+ K- pi+) pi-) K+]cc
#
from Configurables import Generation
Generation().EventType = 14165003
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_BsK+_Dspi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
