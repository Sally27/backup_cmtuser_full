# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/14297012.py generated: Wed, 25 Jan 2017 15:25:31
#
# Event Type: 14297012
#
# ASCII decay Descriptor: [ B_c+ -> (B_s0 -> (D_s+ => K+ K- pi+) (D_s- => pi+ pi- pi-)) pi+]cc
#
from Configurables import Generation
Generation().EventType = 14297012
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_Bspi+_DsDs,KKpi3pi=DDALTIZ,BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
