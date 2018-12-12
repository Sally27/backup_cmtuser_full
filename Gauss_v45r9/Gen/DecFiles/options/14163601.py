# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/14163601.py generated: Fri, 27 Mar 2015 16:10:02
#
# Event Type: 14163601
#
# ASCII decay Descriptor: [B_c+ -> (D_s1(2536)+ ->  (D*(2007)0 -> (D0 -> K- pi+) (pi0 -> gamma gamma)) K+ )  gamma]cc
#
from Configurables import Generation
Generation().EventType = 14163601
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_Ds1gamma,Dst0K,D0pi0,Kpi=DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
from Configurables import BcDaughtersInLHCb
Generation().Special.addTool( BcDaughtersInLHCb )
Generation().Special.BcDaughtersInLHCb.NeutralThetaMin = 0.
Generation().Special.BcDaughtersInLHCb.NeutralThetaMax = 10.
