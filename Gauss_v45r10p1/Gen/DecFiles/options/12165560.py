# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/12165560.py generated: Wed, 25 Jan 2017 15:25:14
#
# Event Type: 12165560
#
# ASCII decay Descriptor: [B+ -> K+ (anti-D*0 -> (anti-D0 -> (K_S0 -> pi+ pi-) K+ K-) (pi0 -> gamma gamma))]cc
#
from Configurables import Generation
Generation().EventType = 12165560
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bu_Dst0K,D0pi0,KSKK=TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 521,-521 ]


from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
Generation().SignalRepeatedHadronization.addTool( LoKi__GenCutTool,'TightCut')
tightCut = Generation().SignalRepeatedHadronization.TightCut
tightCut.Decay = '^[B+ => ^(D*(2007)~0 -> ^(D~0 => ^(KS0 => ^pi+ ^pi-) ^K+ ^K-) ^(pi0 -> ^gamma ^gamma)) ^K+]CC'
tightCut.Preambulo += [
   'GVZ = LoKi.GenVertices.PositionZ()',
   'from GaudiKernel.SystemOfUnits import millimeter',
   'inAcc        = (in_range(0.010, GTHETA, 0.400))',
   'goodB       = (GP > 35000 * MeV) & (GPT > 3500 * MeV) & (GTIME > 0.060 * millimeter)',
   'goodDstar0       = (GP >  25000 * MeV) & (GPT > 4250 * MeV)',
   'goodD0       = (GP >  22500 * MeV) & (GPT > 3750 * MeV)',
   'goodD0K  = (GNINTREE( ("K+"==GABSID) & (GP > 1000 * MeV) & (GPT > 100 * MeV) & inAcc, 1) > 1.5)',
   'goodKSPi  = (GNINTREE( ("pi+"==GABSID) & (GPT >  50 * MeV) & (GP >  1900 * MeV) & inAcc, 1) > 1.5)',
   'goodKS       = (GP >  3500 * MeV) & (GPT > 400 * MeV) ',
   'goodBK = (GNINTREE( ("K+"==GABSID) & (GP > 4500 * MeV) & (GPT > 400 * MeV) & inAcc, 1) > 0.5)',
   'goodPi0Gamma = (GNINTREE( ("gamma"==GABSID) & ( (abs(GPX/GPZ) < 0.315)  &  (abs(GPY/GPZ) < 0.255) & ((abs( GPX/GPZ ) > 0.019)  |  (abs(GPY/GPZ) > 0.019))) , 1) > 0.5)'
]
tightCut.Cuts = {
   '[B+]cc'          : 'goodB & goodBK',
   '[D*(2007)0]cc'   : 'goodDstar0',
   '[pi0]cc'         : 'goodPi0Gamma',
   '[D0]cc'          : 'goodD0 & goodD0K',
   '[KS0]cc'         : 'goodKS & goodKSPi',
   }


# Ad-hoc particle gun code

from Configurables import ParticleGun
pgun = ParticleGun("ParticleGun")
pgun.SignalPdgCode = 521
pgun.DecayTool = "EvtGenDecay"
pgun.GenCutTool = "LoKi::GenCutTool/TightCut"

pgun.addTool( Generation().SignalRepeatedHadronization.TightCut.clone(), "TightCut" )

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
pgun.EventType = 12165560
