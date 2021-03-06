# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11522022.py generated: Wed, 25 Jan 2017 15:25:17
#
# Event Type: 11522022
#
# ASCII decay Descriptor: [B0 => pi- nu_e e+]cc
#
from Configurables import Generation
Generation().EventType = 11522022
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_pienu=TightCut,M4.5GeV.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]

#
from Configurables import LoKi__GenCutTool
Generation().SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' ) 
tightCut  = Generation().SignalRepeatedHadronization.TightCut
#
tightCut.Decay    = "[B0 => pi- e+ nu_e]CC"
tightCut.Cuts     = {
   '[B0]cc'  : "GINTREE((GABSID == 'pi+') & (ACC)) & GINTREE((GABSID == 'e+') & (ACC)) & (BM2 > 20250000.)",
   }
#
tightCut.Preambulo += [
   "BPX2 = (GCHILD(GPX,'pi+' == GABSID) + GCHILD(GPX,'e+' == GABSID))**2",
   "BPY2 = (GCHILD(GPY,'pi+' == GABSID) + GCHILD(GPY,'e+' == GABSID))**2",
   "BPZ2 = (GCHILD(GPZ,'pi+' == GABSID) + GCHILD(GPZ,'e+' == GABSID))**2",
   "BPE2 = (GCHILD(GE ,'pi+' == GABSID) + GCHILD(GE, 'e+' == GABSID))**2",
   "BM2  = (BPE2 - BPX2 - BPY2 - BPZ2)" ,
   "ACC  = in_range ( 0.0075, GTHETA, 0.400 )" , 
   ]

