# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/27163401.py generated: Fri, 27 Mar 2015 16:10:09
#
# Event Type: 27163401
#
# ASCII decay Descriptor: [D*(2010)+ -> ( D0 -> (phi(1020) -> K+ K-) pi0 ) pi+]cc
#
from Configurables import Generation
Generation().EventType = 27163401
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Dst_D0pi,KKpi0=TightCut.dec"
Generation().SignalPlain.CutTool = "'LoKi::GenCutTool/TightCut'"
Generation().SignalPlain.SignalPIDList = [ 413,-413 ]

#
from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
gen = Generation()
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = '[ D*(2010)+ -> ^( D0 -> (phi(1020) -> ^K+ ^K-) ^pi0 ) ^pi+]CC'
tightCut.Preambulo += [
    "from GaudiKernel.SystemOfUnits import MeV       " ,
    "inAcc     = in_range ( 0.005 , GTHETA , 0.400 ) "
]
tightCut.Cuts      =    {
    '[K+]cc'   : 'inAcc & ( 400 * MeV < GPT ) ',
    '[pi+]cc'  : 'inAcc ',
    'pi0'      : '( 800 * MeV < GPT ) '
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
pgun.EventType = 27163401
