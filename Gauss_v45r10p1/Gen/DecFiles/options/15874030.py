# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/15874030.py generated: Wed, 25 Jan 2017 15:25:15
#
# Event Type: 15874030
#
# ASCII decay Descriptor: [ Lambda_b0 ==>  (Lambda_c+ ==> p+ K- pi+)  (tau- -> mu- anti_nu_mu nu_tau) anti_nu_tau   ]cc
#
from Configurables import Generation
Generation().EventType = 15874030
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Lctaunu,pKpi=cocktail,TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]

#
from Configurables import LoKi__GenCutTool
Generation().SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' ) 
tightCut  = Generation().SignalPlain.TightCut
tightCut.Decay = "[ Lambda_b0 =>  (Lambda_c+ ==> ^p+ ^K- ^pi+)  ( tau- -> ^mu- nu_tau nu_mu~) nu_tau~ ]CC"
tightCut.Preambulo += [
"from LoKiCore.functions import in_range"  ,
"from GaudiKernel.SystemOfUnits import GeV, MeV",
"pmuPX = GCHILD(GPX,('p+' == GABSID )) + GCHILD(GPX,('mu-' == GABSID))",
"pmuPY = GCHILD(GPY,('p+' == GABSID )) + GCHILD(GPY,('mu-' == GABSID))",
"pmuPT2 = pmuPX * pmuPX + pmuPY * pmuPY"
 ]
tightCut.Cuts      =    {
'[p+]cc'   : " in_range( 0.010 , GTHETA , 0.400 )& ( GPT > 950 * MeV ) & (GP > 14600 * MeV)" ,
'[mu-]cc'  : " in_range( 0.010 , GTHETA , 0.400 ) & (GPT > 1450 * MeV) &  (GP > 4900 * MeV) ",
'[Lambda_b0]cc' : "pmuPT2 > 1960000"
  }

