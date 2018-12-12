# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/14513002.py generated: Wed, 25 Jan 2017 15:25:16
#
# Event Type: 14513002
#
# ASCII decay Descriptor: [B_c+ -> mu+ mu- mu+ nu_mu]cc
#
from Configurables import Generation
Generation().EventType = 14513002
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_mumumunu=WeightedBcVegPy,DiLeptonInAcc.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "DiLeptonInAcceptance"
