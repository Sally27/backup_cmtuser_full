# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/15104411.py generated: Fri, 27 Mar 2015 15:48:12
#
# Event Type: 15104411
#
# ASCII decay Descriptor: [Lambda_b0 -> K- (eta' -> pi+ pi- (eta -> gamma gamma)) p+]cc
#
from Configurables import Generation
Generation().EventType = 15104411
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_pKetap,etapipi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
