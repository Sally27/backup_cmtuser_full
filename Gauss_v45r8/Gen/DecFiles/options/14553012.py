# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/14553012.py generated: Fri, 27 Mar 2015 15:48:09
#
# Event Type: 14553012
#
# ASCII decay Descriptor: [B_c+ => (J/psi(1S) -> e+ e-) mu+ nu_mu]cc
#
from Configurables import Generation
Generation().EventType = 14553012
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_Jpsimunu,ee=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
