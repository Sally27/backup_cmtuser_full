# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/14285400.py generated: Wed, 25 Jan 2017 15:25:16
#
# Event Type: 14285400
#
# ASCII decay Descriptor: [B_c+ -> (D_s*- -> (D_s- -> K+ K- pi-) pi0) e+ e+]cc
#
from Configurables import Generation
Generation().EventType = 14285400
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_DssteeSS,Kpipi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
