# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/52230100.py generated: Fri, 27 Mar 2015 15:48:05
#
# Event Type: 52210000
#
# ASCII decay Descriptor: mu-,mu+ => ?
#
from Configurables import ParticleGun
from Configurables import MomentumRange
ParticleGun().addTool( MomentumRange )
from GaudiKernel import SystemOfUnits
ParticleGun().MomentumRange.MomentumMin = 100.0*SystemOfUnits.MeV
from GaudiKernel import SystemOfUnits
ParticleGun().MomentumRange.MomentumMax = 100.0*SystemOfUnits.MeV
ParticleGun().EventType = 52230100
ParticleGun().ParticleGunTool = "MomentumRange"
ParticleGun().NumberOfParticlesTool = "FlatNParticles"
ParticleGun().MomentumRange.PdgCodes = [ 13, -13 ]
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/mu+mu-,fixP=TrkAcc.dec"
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/TrackersAcceptance.py" )
