# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/24142001.py generated: Wed, 25 Jan 2017 15:25:31
#
# Event Type: 24142001
#
# ASCII decay Descriptor: J/psi(1S) -> mu+ mu- {,gamma} {,gamma}
#
from Configurables import Generation
Generation().EventType = 24142001
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_Jpsi,mm=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 443 ]

# Ad-hoc particle gun code

from Configurables import ParticleGun
pgun = ParticleGun("ParticleGun")
pgun.SignalPdgCode = 443
pgun.DecayTool = "EvtGenDecay"
pgun.GenCutTool = "DaughtersInLHCb"

from Configurables import FlatNParticles
pgun.NumberOfParticlesTool = "FlatNParticles"
pgun.addTool( FlatNParticles , name = "FlatNParticles" )

from Configurables import MomentumSpectrum
pgun.ParticleGunTool = "MomentumSpectrum"
pgun.addTool( MomentumSpectrum , name = "MomentumSpectrum" )
pgun.MomentumSpectrum.PdgCodes = [ 443 ]
pgun.MomentumSpectrum.InputFile = "$PGUNSDATAROOT/data/Ebeam4000GeV/MomentumSpectrum_443.root"
pgun.MomentumSpectrum.BinningVariables = "ptpz"
pgun.MomentumSpectrum.HistogramPath = "flatPt2y"

from Configurables import BeamSpotSmearVertex
pgun.addTool(BeamSpotSmearVertex, name="BeamSpotSmearVertex")
pgun.VertexSmearingTool = "BeamSpotSmearVertex"
pgun.EventType = 24142001
