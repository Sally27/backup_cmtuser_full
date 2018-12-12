# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/14145004.py generated: Wed, 25 Jan 2017 15:25:34
#
# Event Type: 14145004
#
# ASCII decay Descriptor: [B_c+ -> (psi(2S) -> mu+ mu-) pi+ pi- pi+]cc
#
from Configurables import Generation
Generation().EventType = 14145004
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_psi2Spipipi,mm=BcVegPy,DecProdCut,PHSP.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
