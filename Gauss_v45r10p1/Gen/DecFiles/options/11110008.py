# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11110008.py generated: Wed, 25 Jan 2017 15:25:30
#
# Event Type: 11110008
#
# ASCII decay Descriptor: {[[B0]nos -> (tau+ -> pi+ pi- pi+ anti-nu_tau) (tau- -> mu- anti-nu_mu nu_tau) (K*(892)0 -> K+ pi-)]cc, [[B0]os -> (tau- -> pi+ pi- pi- nu_tau)(tau+ -> pi+ pi- pi+ anti-nu_tau) (K*(892)~0 -> K- pi+)]cc}
#
from Configurables import Generation
Generation().EventType = 11110008
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Ksttautau,3pimu=DecProdCut,TightCut,tauolacleo.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]

from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
gen = Generation()
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay = "[ (Beauty) ==>  ^(K*(892)0 -> ^K+ ^pi-)   ^([tau+ ==> ^pi+ ^pi- ^pi+ nu_tau~]CC) ^([tau- ==> ^mu- nu_mu~   nu_tau]CC) ]CC"
tightCut.Preambulo += [
 "from LoKiCore.functions import in_range"  ,
 "from GaudiKernel.SystemOfUnits import GeV, MeV"  
]
tightCut.Cuts      =    {
'[pi+]cc'   : " in_range( 0.010 , GTHETA , 0.400 ) & ( GPT > 250 * MeV )  " ,
'[K-]cc'   : "  in_range( 0.010 , GTHETA , 0.400 )  & ( GPT > 250 * MeV )" ,
'[mu+]cc'  : " in_range( 0.010 , GTHETA , 0.400 )  & ( GPT > 250 * MeV ) "
   }

