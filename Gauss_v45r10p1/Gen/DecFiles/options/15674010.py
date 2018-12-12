# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/15674010.py generated: Wed, 25 Jan 2017 15:25:23
#
# Event Type: 15674010
#
# ASCII decay Descriptor: {[Lambda_b0 -> (Lambda_c+ => p+ pi+ pi-) mu- nu_mu~]cc}
#
from Configurables import Generation
Generation().EventType = 15674010
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Lcmunu,ppipi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
