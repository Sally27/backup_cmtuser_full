# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/12165595.py generated: Fri, 27 Mar 2015 16:10:06
#
# Event Type: 12165595
#
# ASCII decay Descriptor: [B+ -> K+ (anti-D0 -> (omega -> pi+ pi- (pi0 -> gamma gamma)) (K_S0 -> pi+ pi-))]cc
#
from Configurables import Generation
Generation().EventType = 12165595
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bu_D0K,KSomega=TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 521,-521 ]


from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
Generation().SignalRepeatedHadronization.addTool( LoKi__GenCutTool,'TightCut')
tightCut = Generation().SignalRepeatedHadronization.TightCut
tightCut.Decay = '^[B+ -> ^(D~0 ==> ^(KS0 ==> ^pi+ ^pi-) ^(omega(782) ==>^pi+ ^pi- ^(pi0 ==> ^gamma ^gamma))) ^K+ ]CC'
tightCut.Preambulo += [
   'GVZ = LoKi.GenVertices.PositionZ()',
   'from GaudiKernel.SystemOfUnits import millimeter',
   'inAcc        = (in_range(0.010, GTHETA, 0.300))',
    'inEcalX   = abs ( GPX / GPZ ) < 4.5 / 12.5      ' ,
    'inEcalY   = abs ( GPY / GPZ ) < 3.5 / 12.5      ' ,
   'goodB       = (GP > 7500 * MeV) & (GPT > 1500 * MeV) & (GTIME > 0.105 * millimeter)',
   'goodD0       = (GP >  4000 * MeV) & (GPT > 400 * MeV)',
   'goodOmega      =   (GP >  4000 * MeV) &  (GPT >  400 * MeV)',
   'goodKS       = (GP >  4000 * MeV) & (GPT >  400 * MeV) & (GFAEVX(abs(GVZ),0) < 2500.0 * millimeter)',
   'goodBK = (GNINTREE( ("K+"==GABSID) & (GP > 4000 * MeV) & (GPT > 400 * MeV) & inAcc, 1) > 0.5)',
   'goodKsDaugPi = (GNINTREE( ("pi+"==GABSID) & (GP > 500 * MeV) & (GPT > 50 * MeV) & inAcc, 1) > 1.5)',
   'goodOmegaPi  = (GNINTREE( ("pi+"==GABSID) & (GP > 750 * MeV) & (GPT > 75 * MeV) & inAcc, 1) > 1.5)',
   'goodOmegaPi0   = (GNINTREE( ("pi0"==GABSID) & (GP > 750 * MeV) & (GPT > 400 * MeV) & inAcc, 1) > 0.5)',
   'goodPi0Gamma = (GNINTREE( ("gamma"==GABSID) & (GP > 750 * MeV) & (GPT > 400 * MeV) & inEcalX  & inEcalY  & inAcc, 1) > 1.5)',
]
tightCut.Cuts = {
   '[B+]cc'          : 'goodB & goodBK', 
   '[D0]cc'          : 'goodD0',
   '[KS0]cc'         : 'goodKS & goodKsDaugPi',
   '[omega(782)]cc'    : 'goodOmega & goodOmegaPi & goodOmegaPi0',
   '[pi0]cc'  :'goodPi0Gamma'
   }


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
pgun.EventType = 12165595
