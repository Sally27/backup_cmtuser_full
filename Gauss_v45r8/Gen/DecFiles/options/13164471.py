# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/13164471.py generated: Fri, 27 Mar 2015 15:47:58
#
# Event Type: 13164471
#
# ASCII decay Descriptor: {[[B_s0]nos -> ( D_s0*- => ( D_s- => K+ K- pi-) (pi0 -> gamma gamma))  pi+]cc, [[B_s0]os -> ( D_s0*+ => ( D_s+ => K+ K- pi+) (pi0 -> gamma gamma ) ) pi-]cc}
#
from Configurables import Generation
Generation().EventType = 13164471
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bs_Ds2317pi,KKpi=DecProdCut,TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "'LoKi::GenCutTool/TightCut'"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 531,-531 ]

from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
gen = Generation()
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay = "[ (Beauty) ==>  (D*_s0- ==> (D_s- ==> ^K+ ^K- ^pi-) ^(pi0 -> ^gamma ^gamma)) ^pi+ ]CC"
tightCut.Preambulo += [
 "from LoKiCore.functions import in_range"  ,
 "from GaudiKernel.SystemOfUnits import GeV, MeV"  
]
tightCut.Cuts      =    {
'[pi+]cc'   : " in_range( 0.010 , GTHETA , 0.400 )  " ,
'[K-]cc'   : "  in_range( 0.010 , GTHETA , 0.400 )  " ,
'[pi0]cc'  : "  ( GPT > 350 * MeV ) ",
'gamma'  : " in_range( 0.005 , GTHETA , 0.400 )   ",
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
pgun.EventType = 13164471
