# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/14573102.py generated: Fri, 27 Mar 2015 16:10:06
#
# Event Type: 14573102
#
# ASCII decay Descriptor: [B_c+ -> (D*0 -> (D0 -> K- pi+) gamma) mu+ nu_mu]cc
#
from Configurables import Generation
Generation().EventType = 14573102
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_Dst0munu=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
