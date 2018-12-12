# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/16166043.py generated: Fri, 27 Mar 2015 15:47:58
#
# Event Type: 16166043
#
# ASCII decay Descriptor: [Xi_b0 -> (D+ --> K- pi+ pi+) p+ K- pi-]CC
#
from Configurables import Generation
Generation().EventType = 16166043
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xib0_D+pK-pi-=phsp.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5232,-5232 ]
