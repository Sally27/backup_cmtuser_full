# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/51210034.py generated: Fri, 27 Mar 2015 15:48:05
#
# Event Type: 51210000
#
# ASCII decay Descriptor: e-,e+ => ?
#
from Configurables import ParticleGun
from Configurables import MomentumRange
ParticleGun().addTool( MomentumRange )
from GaudiKernel import SystemOfUnits
ParticleGun().MomentumRange.MomentumMin = 33.8*SystemOfUnits.GeV
from GaudiKernel import SystemOfUnits
ParticleGun().MomentumRange.MomentumMax = 33.8*SystemOfUnits.GeV
ParticleGun().EventType = 51210034
ParticleGun().ParticleGunTool = "MomentumRange"
ParticleGun().NumberOfParticlesTool = "FlatNParticles"
ParticleGun().MomentumRange.PdgCodes = [ 11, -11 ]
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/e+e-,fixP=TrkAcc.dec"
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/TrackersAcceptance.py" )
