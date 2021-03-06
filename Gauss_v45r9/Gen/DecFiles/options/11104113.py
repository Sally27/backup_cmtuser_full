# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11104113.py generated: Fri, 27 Mar 2015 16:10:02
#
# Event Type: 11104113
#
# ASCII decay Descriptor: [B0 -> K+ K- (KS0 -> pi+ pi-)]cc
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/B2KShh.py" )
from Configurables import Generation
Generation().EventType = 11104113
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_K+K-Ks=sqDalitz,tightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCbAndWithDaughAndBCuts"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
