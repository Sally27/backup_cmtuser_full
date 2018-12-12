# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/15336011.py generated: Wed, 25 Jan 2017 15:25:23
#
# Event Type: 15336011
#
# ASCII decay Descriptor: [Lambda_b0 ->  p+ K- (eta_c -> (anti-K*0 -> K- pi+) K+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 15336011
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_etacpK,hhhh=phsp,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
