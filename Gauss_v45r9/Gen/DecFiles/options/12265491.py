# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/12265491.py generated: Fri, 27 Mar 2015 16:10:18
#
# Event Type: 12265491
#
# ASCII decay Descriptor: [B- -> (D0 -> K- pi+ pi- pi+) (K*(892)- -> (pi0 -> gamma gamma) K-)]cc
#
from Configurables import Generation
Generation().EventType = 12265491
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bu_D0Kst+,K3pi,Kpi0=TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 521,-521 ]


from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
Generation().SignalRepeatedHadronization.addTool( LoKi__GenCutTool,'TightCut')
tightCut = Generation().SignalRepeatedHadronization.TightCut
tightCut.Decay = '[B- -> (D0 ==> ^K- ^pi+ ^pi- ^pi+) ^(K*(892)-  -> ^(pi0 ==> ^gamma ^gamma) ^K-)]CC'
tightCut.Preambulo += [
   'GVZ = LoKi.GenVertices.PositionZ()',
   'from GaudiKernel.SystemOfUnits import millimeter',
   'inAcc        = (in_range(0.005, GTHETA, 0.400))',
   'goodB       = (GPT > 1500 * MeV)',
   'goodD0       = (GPT > 400 * MeV)',
   'goodKst       = (GPT > 400 * MeV)',
   'goodPi0      =   (GPT >  300 * MeV)',
   'goodKstK = (GNINTREE( ("K-"==GABSID) & (GPT > 90 * MeV) & inAcc, 1) > 0.5)',
   'goodD0Pi  = (GNINTREE( ("pi+"==GABSID) & (GPT > 90 * MeV) & inAcc, 1) > 2.5)',
   'goodD0K  = (GNINTREE( ("K-"==GABSID) & (GPT > 90 * MeV) & inAcc, 1) > 0.5)',
    'goodPi0Gamma = (GNINTREE( ("gamma"==GABSID) & ( GPT > 200*MeV ) & (  (abs(GPX/GPZ) < 0.315)  &  (abs(GPY/GPZ) < 0.255) & ((abs( GPX/GPZ ) > 0.019)  |  (abs(GPY/GPZ) > 0.019))), 1) > 1.5)'
]
tightCut.Cuts = {
   '[B-]cc'          : 'goodB',
   '[D0]cc'          : 'goodD0 & goodD0Pi & goodD0K',
   '[K*(892)-]cc' :  'goodKst & goodKstK',
   '[pi0]cc'         : 'goodPi0 & goodPi0Gamma' 
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
pgun.EventType = 12265491
