# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/13104102.py generated: Wed, 25 Jan 2017 15:25:21
#
# Event Type: 13104102
#
# ASCII decay Descriptor: [B_s0 -> (KS0 -> pi+ pi-) (KS0 -> pi+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 13104102
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bs_KSKS=DecProdCut,tightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 531,-531 ]

# 
from Configurables import LoKi__GenCutTool 
gen = Generation() 
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' ) 
# 
tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay     = '[^(B_s0 ==> ^(KS0 -> ^pi+ ^pi-) ^(KS0 -> ^pi+ ^pi-))]CC'
tightCut.Cuts      =    {
    '[B_s0]cc'    : ' goodB     ' , 
    'KS0'   : ' goodKs ' , 
    '[pi+]cc'   : ' goodTrack ' }
tightCut.Preambulo += [
    'inAcc     = in_range ( 0.000 , GTHETA , 0.400 ) ' , 
    'goodB     = ( GP > 15 * GeV )   & inAcc            ' , 
    'goodTrack = ( GP >  1.6 * GeV )       ' , 
    'goodKs   = ( GP >  4 * GeV) & (GPT >  300 * MeV ) & inAcc              ' ] 



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
pgun.EventType = 13104102
