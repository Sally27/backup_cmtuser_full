# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/14165041.py generated: Wed, 25 Jan 2017 15:25:25
#
# Event Type: 14165041
#
# ASCII decay Descriptor: [B_c+ -> (B+ -> (anti-D0 -> pi+ K-) pi+ ) pi+ pi- ]cc
#
from Configurables import Generation
Generation().EventType = 14165041
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_Bupipi,D0pi,piK=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
