# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/14103036.py generated: Fri, 27 Mar 2015 16:10:04
#
# Event Type: 14103036
#
# ASCII decay Descriptor: [B_c+ -> pi+ pi- pi+]cc
#
from Configurables import Generation
Generation().EventType = 14103036
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_pipipi=PHSP,BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
