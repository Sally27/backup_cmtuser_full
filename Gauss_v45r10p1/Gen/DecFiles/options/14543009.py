# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/14543009.py generated: Wed, 25 Jan 2017 15:25:22
#
# Event Type: 14543009
#
# ASCII decay Descriptor: [B_c+ -> (J/psi(1S) -> mu+ mu- {,gamma} {,gamma}) mu+ nu_mu]cc
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/BcDiMuonMinMass.py" )
from Configurables import Generation
Generation().EventType = 14543009
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_Jpsimunu,mm=BcVegPy,BcDaughtersInLHCbAndMassCut,M4.5GeV.dec"
Generation().Special.CutTool = "BcDaughtersInLHCbAndMassCut"
