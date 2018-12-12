# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/14575010.py generated: Wed, 25 Jan 2017 15:25:36
#
# Event Type: 14575010
#
# ASCII decay Descriptor: [B_c+ -> ([B_s0]nos -> (D_s- => K+ K- pi-) pi+, [B_s0]os -> (D_s+ -> K+ K- pi+) pi-) anti-nu_mu mu+]cc
#
from Configurables import Generation
Generation().EventType = 14575010
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_Bsmunu,Dspi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
