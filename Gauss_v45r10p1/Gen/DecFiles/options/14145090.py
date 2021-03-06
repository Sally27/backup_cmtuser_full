# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/14145090.py generated: Wed, 25 Jan 2017 15:25:30
#
# Event Type: 14145090
#
# ASCII decay Descriptor: [B_c+ -> (B+ -> (J/psi(1S) -> mu+ mu-) pi+ ) pi+ pi-]cc
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Bc2sVegPyOpts.py" )
from Configurables import Generation
Generation().EventType = 14145090
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc2_Bcpipi,Jpsipi,mm=DecProdCut,BcVegPy.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "B_c+ 77 541 1.0 6.85800000 1.017330e-20 B_c+ 541 0.0003", "B_c- 78 -541 -1.0 6.85800000 1.017330e-20 B_c- -541 0.0003", "B+ 71 521 1.0  6.27400000   5.090000e-13  B+ 521 0.00000000", "B- 72 -521 -1.0  6.27400000   5.090000e-13 B- -521 0.00000000" ]
