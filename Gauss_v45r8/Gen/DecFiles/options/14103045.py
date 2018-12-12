# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/14103045.py generated: Fri, 27 Mar 2015 15:48:08
#
# Event Type: 14103045
#
# ASCII decay Descriptor: [B_c+ -> (B_s0 -> pi+ K-) pi+]cc
#
from Configurables import Generation
Generation().EventType = 14103045
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_Bspi+,Kpi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
