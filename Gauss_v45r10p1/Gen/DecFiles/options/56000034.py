# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/56000034.py generated: Wed, 25 Jan 2017 15:25:18
#
# Event Type: 56000000
#
# ASCII decay Descriptor: gamma => ?
#
from Configurables import ParticleGun
from Configurables import MomentumRange
ParticleGun().addTool( MomentumRange )
from GaudiKernel import SystemOfUnits
ParticleGun().MomentumRange.MomentumMin = 33.8*SystemOfUnits.GeV
from GaudiKernel import SystemOfUnits
ParticleGun().MomentumRange.MomentumMax = 33.8*SystemOfUnits.GeV
ParticleGun().EventType = 56000034
ParticleGun().ParticleGunTool = "MomentumRange"
ParticleGun().NumberOfParticlesTool = "FlatNParticles"
ParticleGun().MomentumRange.PdgCodes = [ 22 ]
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/gamma,fixE=CaloAcc.dec"
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/CaloAcceptance.py" )
