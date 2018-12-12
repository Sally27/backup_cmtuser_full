# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/28196070.py generated: Fri, 27 Mar 2015 16:10:06
#
# Event Type: 28196070
#
# ASCII decay Descriptor: psi(3770) -> D+(K- pi+ pi+)  D-(K+ pi- pi-)
#
from Configurables import Generation
Generation().EventType = 28196070
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/psi3770_D+D-,Kpipi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 30443 ]
