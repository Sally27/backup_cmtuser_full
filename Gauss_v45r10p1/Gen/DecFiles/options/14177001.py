# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/14177001.py generated: Wed, 25 Jan 2017 15:25:19
#
# Event Type: 14177001
#
# ASCII decay Descriptor: [B_c+ -> (J/psi(1S) -> mu+ mu-) (D*(2010)+ -> (D0 -> K- pi+) pi+) (K*(892)0 -> K+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 14177001
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_JpsiDst+Kst,mmD0pi,Kpi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
