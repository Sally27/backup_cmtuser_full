# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/14195511.py generated: Wed, 25 Jan 2017 15:25:26
#
# Event Type: 14195511
#
# ASCII decay Descriptor: [B_c+ -> (D+ -> (K_S0 -> pi+ pi- ) pi+ pi0) (anti-D0 -> K+ pi-) ]cc
#
from Configurables import Generation
Generation().EventType = 14195511
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_D+D0,KSpipi0,Kpi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
