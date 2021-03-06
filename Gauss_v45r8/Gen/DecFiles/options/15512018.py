# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/15512018.py generated: Fri, 27 Mar 2015 15:47:59
#
# Event Type: 15512018
#
# ASCII decay Descriptor: [Lambda_b0 -> p+ mu- anti-nu_mu]cc
#
from Configurables import Generation
Generation().EventType = 15512018
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_pmunu=TightCut,LQCD,M4.5GeV.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]

#
from Configurables import LoKi__GenCutTool
Generation().SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' ) 
tightCut  = Generation().SignalPlain.TightCut

tightCut.Decay = "^[ Lambda_b0 => ^p+ ^mu- nu_mu~  ]CC"

tightCut.Preambulo += [
"from LoKiCore.functions import in_range",
"from GaudiKernel.SystemOfUnits import GeV, MeV" ,
"ACC  = in_range ( 0.0075, GTHETA, 0.400 )"
 ]

tightCut.Cuts      =    {
   '[Lambda_b0]cc': "GMASS('p+'==GABSID,'mu+'==GABSID) > 4.5*GeV",
   '[p+]cc'       : "ACC & (GPT > 700.*MeV) & (GP > 2500*MeV)",
   '[mu-]cc'      : "ACC & (GPT > 700.*MeV) & (GP > 2500*MeV)"
  }

