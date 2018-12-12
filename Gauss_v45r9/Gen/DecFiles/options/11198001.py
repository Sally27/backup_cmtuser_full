# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11198001.py generated: Fri, 27 Mar 2015 16:10:06
#
# Event Type: 11198001
#
# ASCII decay Descriptor: [B0 -> D+ D*(2010)- K*0]cc
#
from Configurables import Generation
Generation().EventType = 11198001
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_DDstKst0,Kpipi,Kpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
