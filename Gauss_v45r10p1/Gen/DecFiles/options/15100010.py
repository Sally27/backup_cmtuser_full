# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/15100010.py generated: Wed, 25 Jan 2017 15:25:27
#
# Event Type: 15100010
#
# ASCII decay Descriptor: [Lambda_b0 -> (D_*s- -> {gamma  (D_s- ->Ks h), {pi0  (D_s- ->Ks h) } p+]cc
#
from Configurables import Generation
Generation().EventType = 15100010
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Dsst+p-,KsPip=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
