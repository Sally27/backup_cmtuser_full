# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/14143006.py generated: Fri, 27 Mar 2015 15:48:05
#
# Event Type: 14143006
#
# ASCII decay Descriptor: [B_c+ -> (psi(2S) -> mu+ mu- ) (a_1+ -> rho0 pi+ )]cc
#
from Configurables import Generation
Generation().EventType = 14143006
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_psi2Sa1,mmrhopi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
