# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/13996202.py generated: Wed, 25 Jan 2017 15:25:33
#
# Event Type: 13996202
#
# ASCII decay Descriptor: [[B_s0] ==> (D_s*- -> (D_s- -> K- K+ pi-) gamma) (D_s*+ -> (D_s+ -> K+ K- pi+) gamma)]cc
#
from Configurables import Generation
Generation().EventType = 13996202
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bs_DD,DD=cocktail,DsmuTightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 531,-531 ]


from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
gen = Generation()
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay = "[B_s0 ==> ^((Charm) -> ^mu+ nu_mu ... ) ^(D_s- -> ^K- ^K+ ^pi-) {X} {X} {X} {X} {X} {X} {X} ]CC"
tightCut.Preambulo += [
"from GaudiKernel.SystemOfUnits import mrad" ,
"FilterD = GNINTREE (GCHARM, HepMC.parents)",
"FromD   = 1 == FilterD",
"BCut = (GTHETA < 400.0*mrad)"

]
tightCut.Cuts    =    {
'[mu+]cc'     : "FromD",
'[B_s0]cc'	: "BCut"
}



# Ad-hoc particle gun code

from Configurables import ParticleGun
pgun = ParticleGun("ParticleGun")
pgun.SignalPdgCode = 531
pgun.DecayTool = "EvtGenDecay"
pgun.GenCutTool = "LoKi::GenCutTool/TightCut"

pgun.addTool( Generation().SignalRepeatedHadronization.TightCut.clone(), "TightCut" )

from Configurables import FlatNParticles
pgun.NumberOfParticlesTool = "FlatNParticles"
pgun.addTool( FlatNParticles , name = "FlatNParticles" )

from Configurables import MomentumSpectrum
pgun.ParticleGunTool = "MomentumSpectrum"
pgun.addTool( MomentumSpectrum , name = "MomentumSpectrum" )
pgun.MomentumSpectrum.PdgCodes = [ 531,-531 ]
pgun.MomentumSpectrum.InputFile = "$PGUNSDATAROOT/data/Ebeam4000GeV/MomentumSpectrum_531.root"
pgun.MomentumSpectrum.BinningVariables = "pteta"
pgun.MomentumSpectrum.HistogramPath = "h_pteta"

from Configurables import BeamSpotSmearVertex
pgun.addTool(BeamSpotSmearVertex, name="BeamSpotSmearVertex")
pgun.VertexSmearingTool = "BeamSpotSmearVertex"
pgun.EventType = 13996202
