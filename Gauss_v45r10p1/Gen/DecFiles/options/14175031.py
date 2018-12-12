# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/14175031.py generated: Wed, 25 Jan 2017 15:25:34
#
# Event Type: 14175031
#
# ASCII decay Descriptor: [B_c+ -> (J/psi(1S) -> mu+ mu-) (D0 -> K- pi+) K+]cc
#
from Configurables import Generation
Generation().EventType = 14175031
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_JpsiD0K,mmKpi=DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
