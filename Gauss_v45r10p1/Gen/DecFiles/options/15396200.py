# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/15396200.py generated: Wed, 25 Jan 2017 15:25:29
#
# Event Type: 15396200
#
# ASCII decay Descriptor: [Lambda_b0 -> K- (Lambda_c+ -> p+ K- pi+) (anti-D*0 -> (anti-D0 ->  K+ pi-) gamma)]cc
#
from Configurables import Generation
Generation().EventType = 15396200
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_LcDstK,Lc_pKpi,Dst_D0gamma=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
