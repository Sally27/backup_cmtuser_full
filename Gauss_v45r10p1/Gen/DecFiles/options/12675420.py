# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/12675420.py generated: Wed, 25 Jan 2017 15:25:14
#
# Event Type: 12675420
#
# ASCII decay Descriptor: [B- -> (Lambda_c+ -> p+ K- pi+ pi0) Myanti-N(1440)- anti-nu_mu mu-]cc
#
from Configurables import Generation
Generation().EventType = 12675420
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bu_LcNstmunu,pX=TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 521,-521 ]

#
from Configurables import LoKi__GenCutTool
Generation().SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' ) 
tightCut  = Generation().SignalRepeatedHadronization.TightCut
tightCut.Decay = "[ B- ==>  (Lambda_c+ ==> p+ {X} {X} {X} {X}) ^p~-  ^mu- nu_mu~ {X} {X} {X} {X}  ]CC"
tightCut.Preambulo += [
"from LoKiCore.functions import in_range"  ,
"from GaudiKernel.SystemOfUnits import GeV, MeV"
 ]
tightCut.Cuts      =    {
'[p+]cc'   : " in_range( 0.010 , GTHETA , 0.400 )& ( GPT > 950 * MeV ) & (GP > 14600 * MeV)" ,
'[mu-]cc'  : " in_range( 0.010 , GTHETA , 0.400 ) & (GPT > 1450 * MeV) &  (GP > 4900 * MeV)"
  }

from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ 
"N(1440)+              636       12212   1.0      1.4400000      2.194041e-24                 N(1440)+           21440      0.00",
"N(1440)~-             637      -12212  -1.0      1.4400000      2.194841e-24                   anti-N(1440)-           -21440      0.00",
"N(1520)+              420        2124   1.0      1.52000000      5.723584e-24                   N(1520)+           21520      0.00",
"N(1520)~-             421       -2124  -1.0      1.52000000     5.723584e-24                   anti-N(1520)-           -21520      0.00",
"N(1535)+              713       22212   1.0      1.53500000      4.388081e-24                   N(1535)+           21535      0.00",
"N(1535)~-             714      -22212  -1.0      1.53500000      4.388081e-24                   anti-N(1535)-           -21535      0.00",
"N(1720)+              775       32124   1.0      1.72000000      2.632849e-24                   N(1720)+           21720      0.00",
"N(1720)~-             776      -32124  -1.0      1.72000000      2.632849e-24                   anti-N(1720)-           -21720      0.00"
]


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
pgun.EventType = 12675420
