# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/27265005.py generated: Fri, 27 Mar 2015 16:10:00
#
# Event Type: 27265005
#
# ASCII decay Descriptor: [D*+ -> (D0 -> K- K+ K- pi+) pi+]cc
#
from Configurables import Generation
Generation().EventType = 27265005
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Dst_D0pi,KKKpi_Res=DecProdCut,CutsForDstar.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCbAndCutsForDstar"
from Configurables import DaughtersInLHCbAndCutsForDstar
Generation().SignalPlain.addTool( DaughtersInLHCbAndCutsForDstar )
from GaudiKernel import SystemOfUnits
Generation().SignalPlain.DaughtersInLHCbAndCutsForDstar.D0PtCuts = 3000*SystemOfUnits.MeV
from GaudiKernel import SystemOfUnits
Generation().SignalPlain.DaughtersInLHCbAndCutsForDstar.DaughtersPtMinCut = 250*SystemOfUnits.MeV
from GaudiKernel import SystemOfUnits
Generation().SignalPlain.DaughtersInLHCbAndCutsForDstar.DaughtersPMinCut = 3000*SystemOfUnits.MeV
Generation().SignalPlain.SignalPIDList = [ 413,-413 ]

# Ad-hoc particle gun code

from Configurables import ParticleGun
pgun = ParticleGun("ParticleGun")
pgun.SignalPdgCode = 413
pgun.DecayTool = "EvtGenDecay"
pgun.GenCutTool = "DaughtersInLHCb"

from Configurables import FlatNParticles
pgun.NumberOfParticlesTool = "FlatNParticles"
pgun.addTool( FlatNParticles , name = "FlatNParticles" )

from Configurables import MomentumSpectrum
pgun.ParticleGunTool = "MomentumSpectrum"
pgun.addTool( MomentumSpectrum , name = "MomentumSpectrum" )
pgun.MomentumSpectrum.PdgCodes = [ 413,-413 ]
pgun.MomentumSpectrum.InputFile = "$PGUNSDATAROOT/data/Ebeam4000GeV/MomentumSpectrum_413.root"
pgun.MomentumSpectrum.BinningVariables = "pteta"
pgun.MomentumSpectrum.HistogramPath = "h_pteta"

from Configurables import BeamSpotSmearVertex
pgun.addTool(BeamSpotSmearVertex, name="BeamSpotSmearVertex")
pgun.VertexSmearingTool = "BeamSpotSmearVertex"
pgun.EventType = 27265005
