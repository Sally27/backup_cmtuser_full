# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/14135004.py generated: Fri, 27 Mar 2015 16:10:06
#
# Event Type: 14135004
#
# ASCII decay Descriptor: [B_c+ -> ([B0]nos -> (J/psi(1S) -> mu+ mu- {,gamma} {,gamma}) (K*(892)0 -> K+ pi-), [B0]os -> (J/psi(1S) -> mu+ mu- {,gamma} {,gamma}) (K*(892)~0 -> K- pi+)) pi+ {,gamma}]cc
#
from Configurables import Generation
Generation().EventType = 14135004
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_Bdpi+_JpsiKstar=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
