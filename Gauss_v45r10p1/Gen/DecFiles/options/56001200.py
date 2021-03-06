# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/56001200.py generated: Wed, 25 Jan 2017 15:25:35
#
# Event Type: 56040000
#
# ASCII decay Descriptor: gamma => ?
#
from Configurables import ParticleGun
from Configurables import MomentumRange
ParticleGun().addTool( MomentumRange )
from GaudiKernel import SystemOfUnits
ParticleGun().MomentumRange.MomentumMin = 400.0*SystemOfUnits.GeV
from GaudiKernel import SystemOfUnits
ParticleGun().MomentumRange.MomentumMax = 1200.0*SystemOfUnits.GeV
ParticleGun().EventType = 56001200
ParticleGun().ParticleGunTool = "MomentumRange"
ParticleGun().NumberOfParticlesTool = "FlatNParticles"
ParticleGun().MomentumRange.PdgCodes = [ 22 ]
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/gamma,contHighE=CaloAcc.dec"
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/CaloAcceptance.py" )
