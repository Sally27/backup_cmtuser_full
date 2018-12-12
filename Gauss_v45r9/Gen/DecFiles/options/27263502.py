# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/27263502.py generated: Fri, 27 Mar 2015 16:10:00
#
# Event Type: 27263502
#
# ASCII decay Descriptor: [D*(2010)+ -> (D0 -> KS0 pi- pi+ pi0) pi+]cc
#
from Configurables import Generation
Generation().EventType = 27263502
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Dst_D0pi,Kstrho,KSpipipi0=CharmForVubCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 413,-413 ]

#
from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
gen = Generation()
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = gen.SignalPlain.TightCut
tightCut.Decay = " [ D*(2010)+ -> ^( D0 --> KS0 ^pi- ^pi+ pi0 ) ^pi+ ]CC"
tightCut.Preambulo += [
  "from LoKiCore.functions import in_range"  ,
  "from LoKiGen.functions import LoKi" ,
  "from LoKiGen.HepMC import descendants" ,
  "from GaudiKernel.SystemOfUnits import GeV, MeV"  ,
  "dipiP     = GCHILD(GP,('pi-' == GID )) + GCHILD(GP,('pi+' == GID ))" ,
  "dipiPT     = GCHILD(GPT,('pi-' == GID )) + GCHILD(GPT,('pi+' == GID ))" ,
  "piPT    = GNINTREE( ('pi-' == GABSID ) & (GPT > 500 * MeV) , 4)", 
]
tightCut.Cuts      =    {
 '[pi+]cc'   : "(in_range( 0.010 , GTHETA , 0.400 ))" ,
 '[D0]cc'   : "( piPT > 1.5 ) & (dipiP > 19000 * MeV) & (dipiPT > 2600 * MeV)" 
    }


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
pgun.EventType = 27263502
