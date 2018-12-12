# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/14375204.py generated: Wed, 25 Jan 2017 15:25:30
#
# Event Type: 14375204
#
# ASCII decay Descriptor: [B_c+ -> (J/psi(1S) -> mu+ mu-) (D*_s+ -> (D_s+ => K+ K- pi+ ) gamma/pi0) ]cc
#
from Configurables import Generation
Generation().EventType = 14375204
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_JpsiDsStar+,mmKKpi=DDalitz,DecProdCut,Az.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
