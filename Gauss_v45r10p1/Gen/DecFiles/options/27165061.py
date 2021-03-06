# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/27165061.py generated: Wed, 25 Jan 2017 15:25:37
#
# Event Type: 27165061
#
# ASCII decay Descriptor: [D_s1(2536)+ -> (D_s+ -> K+ K- pi+) pi+ pi- ]cc
#
from Configurables import Generation
Generation().EventType = 27165061
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds1_Dspipi,KKpi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 10433,-10433 ]
