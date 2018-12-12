# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/14197433.py generated: Wed, 25 Jan 2017 15:25:27
#
# Event Type: 14197433
#
# ASCII decay Descriptor: [B_c+ => (D*_s+ => (D_s+ -> K- K+ pi+) pi0) (D*(2007)~0 => (D~0 -> K+ pi- pi+ pi-) pi0) ]CC
#
from Configurables import Generation
Generation().EventType = 14197433
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_DsstDst0,Dspi0,KKpi,D0pi0,Kpipipi=BcVegPy,DecProdCut,HELAMP010.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
