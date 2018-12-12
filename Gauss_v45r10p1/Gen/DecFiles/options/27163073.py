# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/27163073.py generated: Wed, 25 Jan 2017 15:25:29
#
# Event Type: 27163073
#
# ASCII decay Descriptor: [D*(2010)+ -> (D0 -> pi- pi+) pi+]cc
#
from Configurables import Generation
Generation().EventType = 27163073
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Dst_D0pi,pipi=TightCut,LTUNB.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 413,-413 ]

#
from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
generation = Generation() 
signal     = generation.SignalPlain 
signal.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut   = signal.TightCut
tightCut.Decay     = '[D*(2010)+ -> ^( D0 => ^pi- ^pi+ ) pi+]CC'
tightCut.Preambulo += [
    'from GaudiKernel.SystemOfUnits import millimeter, micrometer,MeV,GeV',
    'GY            =  LoKi.GenParticles.Rapidity () ## to be sure ' , 
    'inAcc         =  in_range ( 0.005 , GTHETA , 0.400 )         ' ,
    'inEta         =  in_range ( 1.95  , GETA   , 5.050 )         ' ,
    'fastTrack     =  ( GPT > 550 * MeV ) & ( GP  > 3.6 * GeV )   ' , 
    'goodTrack     =  inAcc & inEta & fastTrack                   ' ,     
    'inY           =  in_range ( 1.9   , GY     , 4.6   )         ' , 
    'goodD0        =  inY & ( GPT > 1.4 * GeV )                   ' ,
]
tightCut.Cuts     =    {
    '[D0]cc'  : 'goodD0 ' ,
    '[pi-]cc' : 'goodTrack ' , 
    '[pi+]cc' : 'goodTrack '
    }


# Ad-hoc particle gun code

from Configurables import ParticleGun
pgun = ParticleGun("ParticleGun")
pgun.SignalPdgCode = 413
pgun.DecayTool = "EvtGenDecay"
pgun.GenCutTool = "LoKi::GenCutTool/TightCut"

pgun.addTool( Generation().SignalPlain.TightCut.clone(), "TightCut" )

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
pgun.EventType = 27163073
