# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/13512004.py generated: Fri, 27 Mar 2015 16:10:08
#
# Event Type: 13512004
#
# ASCII decay Descriptor: [B_s0 -> (K+ -> mu+ nu_mu) (pi- -> mu- nu_mu~)]cc
#
from Configurables import Generation
Generation().EventType = 13512004
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bs_K+pi-,mm=TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "'LoKi::GenCutTool/TightCut'"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 531,-531 ]

#
from Configurables import LoKi__GenCutTool
gen = Generation()
gen.SignalRepeatedHadronization.setProp('MaxNumberOfRepetitions', 5000 )
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' )
#
tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay     = '[ Beauty -> ^(K+ -> ^mu+ nu_mu) ^(pi- -> ^mu- nu_mu~ )]CC'
tightCut.Preambulo += [
    "GVZ = LoKi.GenVertices.PositionZ() " ,
    "from GaudiKernel.SystemOfUnits import meter, GeV" ,
    "decay = in_range ( -1 * meter,            GFAEVX ( GVZ, 100 * meter ),                    10 * meter ) ",
#   "decay = in_range ( -1 * meter , monitor ( GFAEVX ( GVZ, 100 * meter ) , '  decay-Z\n' ) , 10 * meter ) ",
    "inAcc = in_range ( 0.0075, GTHETA, 0.400 ) " , 
]
tightCut.Cuts      =    {
    '[K+]cc'   : ' decay & inAcc ',
    '[pi+]cc'  : ' decay & inAcc ',
#   '[mu+]cc'  : " 3 * GeV < monitor ( GP , '  mu P\n' )" , 
    '[mu+]cc'  : " 3 * GeV < GP " , 
                        }


# Ad-hoc particle gun code

from Configurables import ParticleGun
pgun = ParticleGun("ParticleGun")
pgun.SignalPdgCode = 531
pgun.DecayTool = "EvtGenDecay"
pgun.GenCutTool = "DaughtersInLHCb"

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
pgun.EventType = 13512004
