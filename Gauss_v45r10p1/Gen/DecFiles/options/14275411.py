# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/14275411.py generated: Wed, 25 Jan 2017 15:25:25
#
# Event Type: 14275411
#
# ASCII decay Descriptor: [B_c+ -> (D_s*- -> (D_s- -> K+ K- pi-) pi0) e+ mu+]cc
#
from Configurables import Generation
Generation().EventType = 14275411
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_DsstemuSS,Kpipi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
