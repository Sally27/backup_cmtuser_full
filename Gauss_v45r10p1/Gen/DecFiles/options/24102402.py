# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/24102402.py generated: Wed, 25 Jan 2017 15:25:34
#
# Event Type: 24102402
#
# ASCII decay Descriptor: J/psi(1S) -> p+ anti-p- pi0
#
from Configurables import Generation
Generation().EventType = 24102402
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_Jpsi,pppi0=Pt0.9GeV,TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 443 ]
 
from Configurables import LoKi__GenCutTool as GenCutTool 
#
Generation().SignalPlain.addTool( GenCutTool , 'TightCut' ) 
Generation().SignalPlain.TightCut.Decay = "J/psi(1S) => ^p+ ^p~- ^pi0"
Generation().SignalPlain.TightCut.Cuts = {
    'p+'  : ' ( GPT > 0.9 * GeV ) & inAcc ',
    'p~-' : ' ( GPT > 0.9 * GeV ) & inAcc ',
    'pi0' : ' noAcc '
    }
Generation().SignalPlain.TightCut.Preambulo += [
    'inAcc   = in_range ( 0.010 , GTHETA , 0.400 ) ',
    'noAcc = in_range (0, GTHETA, 3.15)'
    ]


# Ad-hoc particle gun code

from Configurables import ParticleGun
pgun = ParticleGun("ParticleGun")
pgun.SignalPdgCode = 443
pgun.DecayTool = "EvtGenDecay"
pgun.GenCutTool = "LoKi::GenCutTool/TightCut"

pgun.addTool( Generation().SignalPlain.TightCut.clone(), "TightCut" )

from Configurables import FlatNParticles
pgun.NumberOfParticlesTool = "FlatNParticles"
pgun.addTool( FlatNParticles , name = "FlatNParticles" )

from Configurables import MomentumSpectrum
pgun.ParticleGunTool = "MomentumSpectrum"
pgun.addTool( MomentumSpectrum , name = "MomentumSpectrum" )
pgun.MomentumSpectrum.PdgCodes = [ 443 ]
pgun.MomentumSpectrum.InputFile = "$PGUNSDATAROOT/data/Ebeam4000GeV/MomentumSpectrum_443.root"
pgun.MomentumSpectrum.BinningVariables = "ptpz"
pgun.MomentumSpectrum.HistogramPath = "flatPt2y"

from Configurables import BeamSpotSmearVertex
pgun.addTool(BeamSpotSmearVertex, name="BeamSpotSmearVertex")
pgun.VertexSmearingTool = "BeamSpotSmearVertex"
pgun.EventType = 24102402
