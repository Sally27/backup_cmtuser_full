# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/12163235.py generated: Wed, 25 Jan 2017 15:25:25
#
# Event Type: 12163235
#
# ASCII decay Descriptor: [B- -> (D*0 -> (D0 -> K- pi+) gamma) K-]cc
#
from Configurables import Generation
Generation().EventType = 12163235
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bu_Dst0K,D0gamma,Kpi=TightCut,LooserCuts.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 521,-521 ]


from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
Generation().SignalRepeatedHadronization.addTool( LoKi__GenCutTool,'TightCut')
tightCut = Generation().SignalRepeatedHadronization.TightCut
tightCut.Decay = '^[B- -> ^(D*(2007)0 ==> ^(D0 ==> ^K- ^pi+) ^gamma ) ^K-]CC'
tightCut.Preambulo += [
   'GVZ = LoKi.GenVertices.PositionZ()',
   'from GaudiKernel.SystemOfUnits import millimeter',
   'inAcc        = (in_range(0.010, GTHETA, 0.400))',
   'goodB       = (GP > 7500 * MeV) & (GPT > 1500 * MeV) & (GTIME > 0.010 * millimeter)',
   'goodD0       = (GP >  4000 * MeV) & (GPT > 400 * MeV)',
   'goodDstar0       = (GP >  4000 * MeV) & (GPT > 400 * MeV)',
   'goodGamma      =  (GNINTREE( ("gamma"==GABSID) & ( GPT > 200*MeV ) & (  (abs(GPX/GPZ) < 0.315)  &  (abs(GPY/GPZ) < 0.255) & ((abs( GPX/GPZ ) > 0.019)  |  (abs(GPY/GPZ) > 0.019))), 1) > 0.5)',
   'goodBK = (GNINTREE( ("K+"==GABSID) & (GP > 900 * MeV) & (GPT > 90 * MeV) & inAcc, 1) > 0.5)',
   'goodD0Pi  = (GNINTREE( ("pi+"==GABSID) & (GP > 1000 * MeV) & (GPT > 100 * MeV) & inAcc, 1) > 0.5)',
   'goodD0K  = (GNINTREE( ("K+"==GABSID) & (GP > 1000 * MeV) & (GPT > 100 * MeV) & inAcc, 1) > 0.5)'
]
tightCut.Cuts = {
   '[B-]cc'          : 'goodB & goodBK',
   '[D*(2007)0]cc'          : 'goodDstar0 & goodGamma',
   '[D0]cc'          : 'goodD0 & goodD0Pi & goodD0K'
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
pgun.EventType = 12163235
