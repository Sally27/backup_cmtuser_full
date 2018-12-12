# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/54230100.py generated: Fri, 27 Mar 2015 15:48:08
#
# Event Type: 54210000
#
# ASCII decay Descriptor: K+,K- => ?
#
from Configurables import ParticleGun
from Configurables import MomentumRange
ParticleGun().addTool( MomentumRange )
from GaudiKernel import SystemOfUnits
ParticleGun().MomentumRange.MomentumMin = 100.0*SystemOfUnits.MeV
from GaudiKernel import SystemOfUnits
ParticleGun().MomentumRange.MomentumMax = 100.0*SystemOfUnits.MeV
ParticleGun().EventType = 54230100
ParticleGun().ParticleGunTool = "MomentumRange"
ParticleGun().NumberOfParticlesTool = "FlatNParticles"
ParticleGun().MomentumRange.PdgCodes = [ 321, -321 ]
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/K+K-,fixP=TrkAcc.dec"
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/TrackersAcceptance.py" )
