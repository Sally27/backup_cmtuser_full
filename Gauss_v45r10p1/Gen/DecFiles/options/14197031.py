# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/14197031.py generated: Wed, 25 Jan 2017 15:25:22
#
# Event Type: 14197031
#
# ASCII decay Descriptor: [B_c+ -> (D*+ -> (D0 -> K- pi+) pi+) (anti-D0 -> K+ pi- pi- pi+)]cc
#
from Configurables import Generation
Generation().EventType = 14197031
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_DstD0,Kpi,Kpipipi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
