# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/27393461.py generated: Fri, 27 Mar 2015 15:47:59
#
# Event Type: 27393461
#
# ASCII decay Descriptor: [D'_s1+ -> (D*0 -> (D0 -> K- pi+) pi0) K+]cc
#
from Configurables import Generation
Generation().EventType = 27393461
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds1_Dst0K,D0pi0,Kpi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 10433,-10433 ]
