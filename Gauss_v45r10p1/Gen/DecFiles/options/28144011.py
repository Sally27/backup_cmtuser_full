# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/28144011.py generated: Wed, 25 Jan 2017 15:25:15
#
# Event Type: 28144011
#
# ASCII decay Descriptor: X_1(3872) -> (J/psi(1S) -> mu+ mu- {,gamma} {,gamma}) (rho(770)0 -> pi+ pi- {,gamma} {,gamma})
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/X3872_1PP.py" )
from Configurables import Generation
Generation().EventType = 28144011
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_X38721++,Jpsirho,mm=DecProdCut.dec"
Generation().Special.CutTool = "UpsilonDaughtersInLHCb"
from Configurables import UpsilonDaughtersInLHCb
Generation().Special.addTool( UpsilonDaughtersInLHCb )
Generation().Special.UpsilonDaughtersInLHCb.SignalPID = 9920443

# Ad-hoc particle gun code

from Configurables import ParticleGun
pgun = ParticleGun("ParticleGun")
pgun.SignalPdgCode = 9920443
pgun.DecayTool = "EvtGenDecay"
pgun.GenCutTool = "UpsilonDaughtersInLHCb"

from Configurables import FlatNParticles
pgun.NumberOfParticlesTool = "FlatNParticles"
pgun.addTool( FlatNParticles , name = "FlatNParticles" )

from Configurables import MomentumSpectrum
pgun.ParticleGunTool = "MomentumSpectrum"
pgun.addTool( MomentumSpectrum , name = "MomentumSpectrum" )
pgun.MomentumSpectrum.PdgCodes = [ 9920443 ]
pgun.MomentumSpectrum.InputFile = "$PGUNSDATAROOT/data/Ebeam4000GeV/MomentumSpectrum_9920443.root"
pgun.MomentumSpectrum.BinningVariables = "ptpz"
pgun.MomentumSpectrum.HistogramPath = "flatPt2y"

from Configurables import BeamSpotSmearVertex
pgun.addTool(BeamSpotSmearVertex, name="BeamSpotSmearVertex")
pgun.VertexSmearingTool = "BeamSpotSmearVertex"
pgun.EventType = 28144011
