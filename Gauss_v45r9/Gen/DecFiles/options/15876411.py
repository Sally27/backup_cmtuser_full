# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/15876411.py generated: Fri, 27 Mar 2015 16:10:04
#
# Event Type: 15876411
#
# ASCII decay Descriptor: [ Lambda_b0 ==>  (Lambda(2625)+ ==> (Lambda_c+ ==> p+ K- pi+) pi+ pi- )  mu- anti-nu_mu {X} {X} {X} {X}  ]cc
#
from Configurables import Generation
Generation().EventType = 15876411
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Lcmunu,Lc2625,pX=cocktail,TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]

#
from Configurables import LoKi__GenCutTool
Generation().SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' ) 
tightCut  = Generation().SignalPlain.TightCut
tightCut.Decay = "[ Lambda_b0 ==>  (Lambda_c+ ==> ^p+ {X} {X} {X} {X})  ^mu- nu_mu~ {X} {X} {X} {X} {X}  ]CC"
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

