# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/14103056.py generated: Fri, 27 Mar 2015 15:48:12
#
# Event Type: 14103056
#
# ASCII decay Descriptor: [B_c+ -> (B0 -> K+ pi-) pi+]cc
#
from Configurables import Generation
Generation().EventType = 14103056
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_Bdpi+,Kpi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
