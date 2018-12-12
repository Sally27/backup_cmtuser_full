# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/14175001.py generated: Fri, 27 Mar 2015 15:47:59
#
# Event Type: 14175001
#
# ASCII decay Descriptor: [B_c+ -> (J/psi(1S) -> mu+ mu- )  ( D_s+ -> ( phi(2010) -> K+ K- ) pi+ )]cc
#
from Configurables import Generation
Generation().EventType = 14175001
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_JpsiDs+,mmKKpi=DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
