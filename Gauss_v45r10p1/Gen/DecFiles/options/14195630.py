# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/14195630.py generated: Wed, 25 Jan 2017 15:25:36
#
# Event Type: 14195630
#
# ASCII decay Descriptor: [B_c+ => (D*(2010)+ => (D+ -> K- pi+ pi+) pi0) (D*(2007)~0 => (D~0 -> K+ pi-) gamma) ]CC
#
from Configurables import Generation
Generation().EventType = 14195630
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_DstDst0,D+pi0,Kpipi,D0gamma,Kpi=BcVegPy,DecProdCut,HELAMP101.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
