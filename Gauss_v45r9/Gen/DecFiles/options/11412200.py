# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11412200.py generated: Fri, 27 Mar 2015 16:10:03
#
# Event Type: 11412200
#
# ASCII decay Descriptor: [B0 -> mu+ mu- eta]cc
#
from Configurables import Generation
Generation().EventType = 11412200
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_etamumu=MS,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
