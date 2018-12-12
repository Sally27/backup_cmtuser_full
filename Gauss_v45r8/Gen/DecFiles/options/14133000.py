# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/14133000.py generated: Fri, 27 Mar 2015 15:48:06
#
# Event Type: 14133000
#
# ASCII decay Descriptor: [B_c+ -> (eta_c(1S) -> p+ p~-) pi+]cc
#
from Configurables import Generation
Generation().EventType = 14133000
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_etacpi,pp=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
