# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/13102423.py generated: Wed, 25 Jan 2017 15:25:15
#
# Event Type: 13102423
#
# ASCII decay Descriptor: {[[B_s0]nos -> K+ pi- (pi0 -> gamma gamma)]cc, [[B_s0]os -> K- pi+ (pi0 -> gamma gamma)]cc}
#
from Configurables import Generation
Generation().EventType = 13102423
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bs_K+pi-pi0=TightCuts,sqDalitz.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 531,-531 ]

# 
from Configurables import LoKi__GenCutTool 
gen = Generation() 
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' ) 
# 
tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay     = '[^(B_s0 => ^K+ ^pi- ^(pi0 -> ^gamma ^gamma))]CC'
tightCut.Cuts      =    {
    '[B_s0]cc'  : ' goodB     ' , 
    '[K+]cc'    : ' goodTrack ' , 
    '[pi-]cc'   : ' goodTrack ' , 
    'pi0'       : ' goodPi0   ' ,
    'gamma'     : ' goodGamma ' }
tightCut.Preambulo += [
    'inAcc     = in_range ( 0.005 , GTHETA , 0.400 ) ' , 
    'inEcalX   = abs ( GPX / GPZ ) < 4.5 / 12.5      ' , 
    'inEcalY   = abs ( GPY / GPZ ) < 3.5 / 12.5      ' , 
    'goodB     = ( GPT > 2500 * MeV )                ' , 
    'goodTrack = ( GPT >  495 * MeV ) & inAcc        ' , 
    'goodPi0   = ( GPT >  800 * MeV )                ' , 
    'goodGamma = ( GPZ > 0 ) & inEcalX & inEcalY     ' ]



# Ad-hoc particle gun code

from Configurables import ParticleGun
pgun = ParticleGun("ParticleGun")
pgun.SignalPdgCode = 531
pgun.DecayTool = "EvtGenDecay"
pgun.GenCutTool = "LoKi::GenCutTool/TightCut"

pgun.addTool( Generation().SignalRepeatedHadronization.TightCut.clone(), "TightCut" )

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
pgun.EventType = 13102423
