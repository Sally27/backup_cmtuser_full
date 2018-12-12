# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/14135005.py generated: Fri, 27 Mar 2015 16:10:02
#
# Event Type: 14135005
#
# ASCII decay Descriptor: [B_c+ -> ([B0]nos -> (J/psi(1S) -> mu+ mu- {,gamma} {,gamma}) (K*(892)0 -> K+ pi-), [B0]os -> (J/psi(1S) -> mu+ mu- {,gamma} {,gamma}) (K*(892)~0 -> K- pi+)) K+ {,gamma}]cc
#
from Configurables import Generation
Generation().EventType = 14135005
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_BdK+_JpsiKstar=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
