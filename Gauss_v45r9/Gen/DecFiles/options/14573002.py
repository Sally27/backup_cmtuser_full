# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/14573002.py generated: Fri, 27 Mar 2015 16:10:14
#
# Event Type: 14573002
#
# ASCII decay Descriptor: [B_c+ -> (D0 -> K- pi+) mu+ nu_mu]cc
#
from Configurables import Generation
Generation().EventType = 14573002
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_D0munu=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
