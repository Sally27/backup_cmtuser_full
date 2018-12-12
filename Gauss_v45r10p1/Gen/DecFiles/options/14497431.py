# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/14497431.py generated: Wed, 25 Jan 2017 15:25:25
#
# Event Type: 14497431
#
# ASCII decay Descriptor: [( B_c+ => (D*(2010)+ => (D+ -> K- pi+ pi+) (gamma||pi0) ) (D~0 -> K+ pi- pi+ pi-) ) || ( B_c+ => (D+ -> K- pi+ pi+) (D*(2007)~0 => (D~0 -> K+ pi- pi+ pi-) (gamma||pi0) ) )]CC
#
from Configurables import Generation
Generation().EventType = 14497431
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_D+Dst0,Kpipi,Kpipipi=SVS,BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
