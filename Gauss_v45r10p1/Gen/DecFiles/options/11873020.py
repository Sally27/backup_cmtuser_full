# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11873020.py generated: Wed, 25 Jan 2017 15:25:35
#
# Event Type: 11873020
#
# ASCII decay Descriptor: {[[B0]nos ==> nu_mu mu+ (D~0 -> K+ pi-) ]cc, [[B0]os => anti_nu_mu mu- (D0 -> K- pi+) ]cc}
#
from Configurables import Generation
Generation().EventType = 11873020
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D0DsX,taunu=cocktail,TightCuts.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]

from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
gen = Generation()
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay = "[ (Beauty) ==> ^(D~0 -> ^K+ ^pi- {gamma} {gamma} {gamma}) ^mu+ nu_mu {X} {X} {X} {X} {X} {X} {X} {X} ]CC"
tightCut.Preambulo += [
 "from LoKiCore.functions import in_range"  ,
 "from GaudiKernel.SystemOfUnits import GeV, MeV"  ,
 "piKP     = GCHILD(GP,('K+' == GABSID )) + GCHILD(GP,('pi-' == GABSID ))" ,
 "piKPT     = GCHILD(GPT,('K+' == GABSID )) + GCHILD(GPT,('pi-' == GABSID ))" ,
]
tightCut.Cuts      =    {
'[pi+]cc'   : " in_range( 0.010 , GTHETA , 0.400 )& ( GPT > 700 * MeV )" ,
'[K-]cc'   : " in_range( 0.010 , GTHETA , 0.400 ) & ( GPT > 700 * MeV )" ,
'[mu+]cc'  : " in_range( 0.010 , GTHETA , 0.400 ) & (GP > 2500* MeV) ",
'[D~0]cc'   : "( piKP > 15000 * MeV ) & (piKPT > 2300 * MeV)"
   }

