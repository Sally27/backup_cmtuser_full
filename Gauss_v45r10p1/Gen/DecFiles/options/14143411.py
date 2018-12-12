# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/14143411.py generated: Wed, 25 Jan 2017 15:25:31
#
# Event Type: 14143411
#
# ASCII decay Descriptor: [B_c+ -> (Jpsi -> mu+ mu-) (K*+ -> (pi0 -> gamma gamma) K+ )]cc
#
from Configurables import Generation
Generation().EventType = 14143411
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_JpsiKst,mm,pi0K,gg=DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
