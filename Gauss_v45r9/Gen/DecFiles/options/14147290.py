# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/14147290.py generated: Fri, 27 Mar 2015 16:10:02
#
# Event Type: 14147290
#
# ASCII decay Descriptor: [B_c+ -> (B*+ -> (B+ -> (J/psi(1S) -> mu+ mu-) pi+ pi+ pi- ) gamma ) pi+ pi-]cc
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Bc2sstarVegPyOpts.py" )
from Configurables import Generation
Generation().EventType = 14147290
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc2st_Bcstpipi,Bcgamma,Jpsipipipi,mm=DecProdCut,BcVegPy,BC_VHAD.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "B_c+ 77 541 1.0  6.89000000   9.192903e-21 B_c+ 541 0.00036", "B_c- 78 -541 -1.0  6.89000000   9.192903e-21 B_c- -541 0.00036", "B+ 71 521 1.0  6.27400000   5.090000e-13  B+ 521 0.00000000", "B- 72 -521 -1.0  6.27400000   5.090000e-13 B- -521 0.00000000", "B*- 187 -523 -1.0 6.34100000   8.227648e-18 B*- -523  0.000004", "B*+ 188 523 1.0 6.34100000   8.227648e-18 B*+ 523  0.000004" ]
