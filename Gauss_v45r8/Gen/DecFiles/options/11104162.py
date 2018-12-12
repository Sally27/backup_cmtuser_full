# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11104162.py generated: Fri, 27 Mar 2015 15:48:12
#
# Event Type: 11104162
#
# ASCII decay Descriptor: [B0 -> (KS0 -> pi+ pi-) p+ p~-]cc
#
from Configurables import Generation
Generation().EventType = 11104162
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Kspp=sqDalitz.dec"
Generation().SignalRepeatedHadronization.CutTool = "LHCbAcceptance"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
