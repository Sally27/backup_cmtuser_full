# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/12667001.py generated: Fri, 27 Mar 2015 15:47:59
#
# Event Type: 12667001
#
# ASCII decay Descriptor: {[B- -> (D_1(2420)0 -> (D*(2010)+ -> (D0 -> K- pi+) pi+ ) pi-) (tau- -> pi- pi+ pi- nu_tau) anti-nu_tau]cc, [B- -> (D_1(H)0 -> (D*(2010)+ -> (D0 -> K- pi+) pi+ ) pi-) (tau- -> pi- pi+ pi- nu_tau) anti-nu_tau]cc, [B- -> (D*_2(2460)0 -> (D*(2010)+ -> (D0 -> K- pi+) pi+ ) pi-) (tau- -> pi- pi+ pi- nu_tau) anti-nu_tau]cc}
#
from Configurables import Generation
Generation().EventType = 12667001
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bu_DststTauNu,Dstpi,D0pi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 521,-521 ]

# Ad-hoc particle gun code

from Configurables import ParticleGun
pgun = ParticleGun("ParticleGun")
pgun.SignalPdgCode = 521
pgun.DecayTool = "EvtGenDecay"
pgun.GenCutTool = "DaughtersInLHCb"

from Configurables import FlatNParticles
pgun.NumberOfParticlesTool = "FlatNParticles"
pgun.addTool( FlatNParticles , name = "FlatNParticles" )

from Configurables import MomentumSpectrum
pgun.ParticleGunTool = "MomentumSpectrum"
pgun.addTool( MomentumSpectrum , name = "MomentumSpectrum" )
pgun.MomentumSpectrum.PdgCodes = [ 521,-521 ]
pgun.MomentumSpectrum.InputFile = "$PGUNSDATAROOT/data/Ebeam4000GeV/MomentumSpectrum_521.root"
pgun.MomentumSpectrum.BinningVariables = "pteta"
pgun.MomentumSpectrum.HistogramPath = "h_pteta"

from Configurables import BeamSpotSmearVertex
pgun.addTool(BeamSpotSmearVertex, name="BeamSpotSmearVertex")
pgun.VertexSmearingTool = "BeamSpotSmearVertex"
pgun.EventType = 12667001
