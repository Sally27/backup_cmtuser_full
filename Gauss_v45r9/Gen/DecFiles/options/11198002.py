# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11198002.py generated: Fri, 27 Mar 2015 16:10:07
#
# Event Type: 11198002
#
# ASCII decay Descriptor: [B0 -> D*(2010)+ D*(2010)- K*0]cc
#
from Configurables import Generation
Generation().EventType = 11198002
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_DstDstKst0,Kpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
