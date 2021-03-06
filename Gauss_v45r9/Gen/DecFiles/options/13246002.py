# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/13246002.py generated: Fri, 27 Mar 2015 16:10:05
#
# Event Type: 13246002
#
# ASCII decay Descriptor: [B_s0 ==> (J/psi(1S) => mu+ mu-) K+ K- pi+ pi-]CC
#
from Configurables import Generation
Generation().EventType = 13246002
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bs_JpsiKKpipi,mm=TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 531,-531 ]

# 
from Configurables import LoKi__GenCutTool 
gen = Generation() 
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' ) 
# 
tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay     = ' ^( ( Beauty & Strange ) ==> ^( J/psi(1S) => ^mu+ ^mu- ) ^K+ ^K- ^pi+ ^pi- ) '
tightCut.Cuts      = {
    '[mu+]cc'             : ' goodMuon  ' , 
    '[K+]cc'              : ' goodKaon  ' , 
    '[pi+]cc'             : ' goodPion  ' , 
    'J/psi(1S)'           : ' goodPsi   ' , 
    '[B_s0]cc'            : ' goodB     ' 
    }

tightCut.Preambulo += [
    'from GaudiKernel.SystemOfUnits import micrometer              ',
    'GY         = LoKi.GenParticles.Rapidity () ## to be 100% sure ', 
    'inAcc      = in_range ( 0.005 , GTHETA , 0.400 ) & in_range ( 1.8 , GETA , 5.2 ) ' , 
    'inY        = in_range ( 1.9   , GY     , 4.6   ) ' , 
    'longLived  = 75 * micrometer < GTIME             ' , 
    'goodMuon   = ( GPT > 500  * MeV ) & ( GP > 6.0 * GeV ) & inAcc ' , 
    'goodKaon   = ( GPT > 150  * MeV ) & ( GP > 2.5 * GeV ) & inAcc ' , 
    'goodPion   = ( GPT > 150  * MeV ) & ( GP > 2.5 * GeV ) & inAcc ' , 
    'goodPsi    =                                             inY   ' ,
    'goodB      = longLived                                 & inY   ' 
    ]



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
pgun.EventType = 13246002
