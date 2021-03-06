# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11574401.py generated: Wed, 25 Jan 2017 15:25:27
#
# Event Type: 11574401
#
# ASCII decay Descriptor: {[[B0]nos => nu_mu mu+ (D*(2010)- => (D- -> K+ pi- pi-) pi0)]cc, [[B0]os => anti_nu_mu mu- (D*(2010)+ => (D+ -> K- pi+ pi+) pi0)]cc}
#
from Configurables import Generation
Generation().EventType = 11574401
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dst+taunu,D+pi,mununu=RDplusCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]

from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
gen = Generation()
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay = "[ (Beauty) ==> ^(D- -> ^K+ ^pi- ^pi- {gamma} {gamma} {gamma}) ^mu+ nu_mu {X} {X} {X} {X} {X} {X} {X} {X} ]CC"
tightCut.Preambulo += [
 "from LoKiCore.functions import in_range"  ,
 "from GaudiKernel.SystemOfUnits import GeV, MeV"  ,
 "pipiKP     = GCHILD(GP,1) + GCHILD(GP,2) + GCHILD(GP,3)" ,
 "pipiKPT     = GCHILD(GPT,1) + GCHILD(GPT,2) + GCHILD(GPT,3)" ,
]
tightCut.Cuts      =    {
'[pi+]cc'   : " in_range( 0.010 , GTHETA , 0.400 )& ( GPT > 150 * MeV )" ,
'[K-]cc'   : " in_range( 0.010 , GTHETA , 0.400 ) & ( GPT > 150 * MeV )" ,
'[mu+]cc'  : " in_range( 0.010 , GTHETA , 0.400 ) & (GP > 2500* MeV) ",
'[D+]cc'   : "( pipiKP > 15000 * MeV ) & (pipiKPT > 2300 * MeV)"
   }

