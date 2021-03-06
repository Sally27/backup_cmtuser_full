# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11566430.py generated: Wed, 25 Jan 2017 15:25:31
#
# Event Type: 11566430
#
# ASCII decay Descriptor: {[[B0]nos => pi+ pi- pi+ (D*(2010)- => (D~0 -> K+ pi-) pi-)]cc, [[B0]os => pi- pi+ pi- (D*(2010)+ => (D0 -> K- pi+) pi+)]cc}
#
from Configurables import Generation
Generation().EventType = 11566430
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dststtaunu,tau3pi,Dst+=cocktail,TightCuts.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]

from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
gen = Generation()
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay = "[ (Beauty) ==> ^(D~0 -> ^K+ ^pi- {gamma} {gamma} {gamma}) ^pi+ ^pi- ^pi+ {X} {X} {X} {X} {X} {X} ]CC"
tightCut.Preambulo += [
 "from LoKiCore.functions import in_range"  ,
 "from GaudiKernel.SystemOfUnits import GeV, MeV"  ,
 "piKP     = GCHILD(GP,('K+' == GABSID )) + GCHILD(GP,('pi-' == GABSID ))" ,
 "piKPT     = GCHILD(GPT,('K+' == GABSID )) + GCHILD(GPT,('pi-' == GABSID ))" ,
]
tightCut.Cuts      =    {
'[pi+]cc'   : " in_range( 0.010 , GTHETA , 0.400 )& ( GPT > 250 * MeV )" ,
'[K-]cc'   : " in_range( 0.010 , GTHETA , 0.400 ) & ( GPT > 250 * MeV )" ,
   }

