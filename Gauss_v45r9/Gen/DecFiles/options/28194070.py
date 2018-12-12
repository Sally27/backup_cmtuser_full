# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/28194070.py generated: Fri, 27 Mar 2015 16:10:03
#
# Event Type: 28194070
#
# ASCII decay Descriptor: psi(3770) -> D0(K- pi+)  D0bar(K+ pi-)
#
from Configurables import Generation
Generation().EventType = 28194070
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/psi3770_D0D0bar,Kpi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 30443 ]
