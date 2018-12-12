# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/15512012.py generated: Fri, 27 Mar 2015 15:48:06
#
# Event Type: 15512012
#
# ASCII decay Descriptor: [Lambda_b~0 => p~- mu+ nu_mu]cc
#
from Configurables import Generation
Generation().EventType = 15512012
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_pmunu=DecProdCut,M4.5GeV.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]

#
from Configurables import LoKi__GenCutTool
Generation().SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' ) 
tightCut  = Generation().SignalPlain.TightCut
#
tightCut.Decay    = "[Lambda_b~0 => p~- mu+ nu_mu]CC"
tightCut.Cuts     = {
   '[Lambda_b0]cc'  : "GINTREE((GABSID == 'p+') & (ACC)) & GINTREE((GABSID == 'mu+') & (ACC)) & (BM2 > 20250000.)",
   }
#
tightCut.Preambulo += [
   "BPX2 = (GCHILD(GPX,'p+' == GABSID) + GCHILD(GPX,'mu+' == GABSID))**2",
   "BPY2 = (GCHILD(GPY,'p+' == GABSID) + GCHILD(GPY,'mu+' == GABSID))**2",
   "BPZ2 = (GCHILD(GPZ,'p+' == GABSID) + GCHILD(GPZ,'mu+' == GABSID))**2",
   "BPE2 = (GCHILD(GE ,'p+' == GABSID) + GCHILD(GE, 'mu+' == GABSID))**2",
   "BM2  = (BPE2 - BPX2 - BPY2 - BPZ2)" ,
   "ACC  = in_range ( 0.0075, GTHETA, 0.400 )" , 
   ]

