# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/14133010.py generated: Fri, 27 Mar 2015 15:48:10
#
# Event Type: 14133010
#
# ASCII decay Descriptor: [B_c+ -> (J/psi(1S) -> p+ p~-) pi+]cc
#
from Configurables import Generation
Generation().EventType = 14133010
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_Jpsipi,pp=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
