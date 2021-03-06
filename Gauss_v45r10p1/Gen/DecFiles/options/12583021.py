# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/12583021.py generated: Wed, 25 Jan 2017 15:25:36
#
# Event Type: 12583021
#
# ASCII decay Descriptor: [B+ -> My_anti-D0 e+ nu_e]cc
#
from Configurables import Generation
Generation().EventType = 12583021
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bu_D0enu,Kenu=DecProdCut,TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 521,-521 ]

#
from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
Generation().SignalRepeatedHadronization.addTool( LoKi__GenCutTool,'TightCut')
tightCut = Generation().SignalRepeatedHadronization.TightCut

tightCut.Decay     = "^[ B+ ==> ^(D~0 ==> ^K+ ^e- nu_e~) ^e+ nu_e ]CC"
tightCut.Cuts      =    {
    '[e-]cc'             : " inAcc & ( GPT > 200 * MeV )  " ,
    '[K+]cc'             : " inAcc & ( GPT > 200 * MeV )  " ,
    '[e+]cc'             : " inAcc & ( GPT > 200 * MeV )  " ,
    '[B+]cc'             : " massCut "
}
tightCut.Preambulo += [
    "from LoKiCore.functions import in_range",
    "from GaudiKernel.SystemOfUnits import GeV, MeV",
    "inAcc      = in_range ( 0.005 , GTHETA , 0.400 ) ",
    "massCut    = GMASS('e-'==GID,'e+'==GID,'K+'==GID) > 4000 * MeV "]



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
pgun.EventType = 12583021
