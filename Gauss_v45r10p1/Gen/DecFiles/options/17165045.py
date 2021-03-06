# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/17165045.py generated: Wed, 25 Jan 2017 15:25:20
#
# Event Type: 17165045
#
# ASCII decay Descriptor: [B_1(L)+ ->  ([B_s0]nos -> (D_s- -> K+ K- pi-) pi+, [B_s0]os -> (D_s+ -> K+ K- pi+) pi-) pi+]cc
#
from Configurables import Generation
Generation().EventType = 17165045
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/X5758+_Bspi+,Dspi,KKpi=DecProdCut,PPChange,TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 10523,-10523 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "B_1(L)+               195       10523   1.0      5.7580000      0.263300e-23                      B_1+       10523      0.25000000", "B_1(L)-               199      -10523  -1.0      5.7580000      0.263300e-23                      B_1-      -10523      0.25000000" ]


from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
gen = Generation()
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay =   "[ B_1(L)+ => ^( ^( Beauty => (D_s- => ^K+ ^K- ^pi-)   ^pi+ ) || ^( Beauty => (D_s+ => ^K- ^K+ ^pi+)   ^pi- ) ) ^pi+]CC"
tightCut.Preambulo += [
 "from LoKiCore.functions import in_range"  ,
 "from GaudiKernel.SystemOfUnits import GeV, MeV"  
]
tightCut.Cuts      =    {
'[pi+]cc'  : " in_range( 0.010 , GTHETA , 0.400 )  " ,
'[K-]cc'   : "  in_range( 0.010 , GTHETA , 0.400 )  " ,
'[B_s0]cc' : "  ( GPT > 4000 * MeV ) ",
   }

