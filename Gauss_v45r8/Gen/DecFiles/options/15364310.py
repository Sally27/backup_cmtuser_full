# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/15364310.py generated: Fri, 27 Mar 2015 15:47:58
#
# Event Type: 15364310
#
# ASCII decay Descriptor: [Lambda_b0 -> (D_*s- -> {gamma  (D_s- ->KS0 K-), {pi0  (D_s- ->KS0 K-) }) p+]cc
#
from Configurables import Generation
Generation().EventType = 15364310
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Dsstp_KSK=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
