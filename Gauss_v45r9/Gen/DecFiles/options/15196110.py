# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/15196110.py generated: Fri, 27 Mar 2015 16:10:13
#
# Event Type: 15196110
#
# ASCII decay Descriptor: [Lambda_b0 -> (psi(3770) ->  (D0 -> K- pi+) (D0bar -> K+ pi-) ) (Lambda0 -> p+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 15196110
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_psi3770Lambda,D0D0bar,Kpi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
