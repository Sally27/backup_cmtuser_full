# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/54210010.py generated: Fri, 27 Mar 2015 15:48:08
#
# Event Type: 54210000
#
# ASCII decay Descriptor: K+,K- => ?
#
from Configurables import ParticleGun
from Configurables import MomentumRange
ParticleGun().addTool( MomentumRange )
from GaudiKernel import SystemOfUnits
ParticleGun().MomentumRange.MomentumMin = 10.0*SystemOfUnits.GeV
from GaudiKernel import SystemOfUnits
ParticleGun().MomentumRange.MomentumMax = 10.0*SystemOfUnits.GeV
ParticleGun().EventType = 54210010
ParticleGun().ParticleGunTool = "MomentumRange"
ParticleGun().NumberOfParticlesTool = "FlatNParticles"
ParticleGun().MomentumRange.PdgCodes = [ 321, -321 ]
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/K+K-,fixP=TrkAcc.dec"
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/TrackersAcceptance.py" )
