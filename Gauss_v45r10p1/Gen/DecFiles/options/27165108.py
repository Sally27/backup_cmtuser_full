# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/27165108.py generated: Wed, 25 Jan 2017 15:25:33
#
# Event Type: 27165108
#
# ASCII decay Descriptor: [D*(2010)+ -> (D0 -> (KS0 -> pi+ pi-) K+ K-) pi+]cc
#
from Configurables import Generation
Generation().EventType = 27165108
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Dst_D0pi,KSKK=mix,TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 413,-413 ]

#
from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
gen = Generation()
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = '^[ D*(2010)+ -> ^( D0 => ^( KS0 => ^pi+ ^pi- ) ^K+ ^K- ) ^pi+]CC'
tightCut.Preambulo += [
    'GVZ = LoKi.GenVertices.PositionZ() ' ,
    'from GaudiKernel.SystemOfUnits import millimeter ',
    'inAcc     = in_range ( 0.005 , GTHETA , 0.400 ) ',
    'goodD0    = ( GPT > 2000 * MeV) & (GTIME > 0.075 * millimeter) & (GFAEVX( abs( GVZ  ) , 0 )  <  8000.0 * millimeter ) ',
    'kaoncuts  = ( GNINTREE( ("K+" == GABSID ) & (GP > 1500 * MeV) , 4) > 1.5 )',
    'pioncuts  = ( GNINTREE( ("pi+" == GABSID ) & (GP > 1500 * MeV) , 4) > 1.5 )',
    'goodKS    = ( GFAEVX( abs( GVZ  ) , 0 )  <  800.0 * millimeter ) ',
    'goodDst   = ( (GPT > 1500 * MeV) & (GPT < (3 * GP / 10)) & (GPT > (7*GP/300 - 7/3)) ) ',
    'trigger   = ( GNINTREE( (("pi+" == GABSID) | ("K+" == GABSID)) & (GPT > 1400 * MeV ) & (GP > 2700 * MeV) , 4)  > 0.5) ',
]
tightCut.Cuts      =    {
    '[pi+]cc'   : 'inAcc',
    '[K+]cc'    : 'inAcc',
    '[D0]cc'    : 'goodD0 & pioncuts & trigger',
    '[D*(2010)+]cc' : 'goodDst',
    'KS0'       : 'goodKS',
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
pgun.EventType = 27165108
