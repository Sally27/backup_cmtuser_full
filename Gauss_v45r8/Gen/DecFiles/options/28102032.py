# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/28102032.py generated: Fri, 27 Mar 2015 15:48:13
#
# Event Type: 28102032
#
# ASCII decay Descriptor: [chi_c0 -> p+ p~-]
#
from Configurables import Generation
Generation().EventType = 28102032
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/chic0_pp.dec"
Generation().SignalPlain.CutTool = ""
Generation().SignalPlain.SignalPIDList = [ 10441 ]

# Ad-hoc particle gun code

from Configurables import ParticleGun
pgun = ParticleGun("ParticleGun")
pgun.SignalPdgCode = 10441
pgun.DecayTool = "EvtGenDecay"
pgun.GenCutTool = "DaughtersInLHCb"

from Configurables import FlatNParticles
pgun.NumberOfParticlesTool = "FlatNParticles"
pgun.addTool( FlatNParticles , name = "FlatNParticles" )

from Configurables import MomentumSpectrum
pgun.ParticleGunTool = "MomentumSpectrum"
pgun.addTool( MomentumSpectrum , name = "MomentumSpectrum" )
pgun.MomentumSpectrum.PdgCodes = [ 10441 ]
pgun.MomentumSpectrum.InputFile = "$PGUNSDATAROOT/data/Ebeam4000GeV/MomentumSpectrum_10441.root"
pgun.MomentumSpectrum.BinningVariables = "ptpz"
pgun.MomentumSpectrum.HistogramPath = "OutputMomentumSpectrum_ptpz"

from Configurables import BeamSpotSmearVertex
pgun.addTool(BeamSpotSmearVertex, name="BeamSpotSmearVertex")
pgun.VertexSmearingTool = "BeamSpotSmearVertex"
pgun.EventType = 28102032
