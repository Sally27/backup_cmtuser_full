# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11102422.py generated: Fri, 27 Mar 2015 16:10:08
#
# Event Type: 11102422
#
# ASCII decay Descriptor: {[[B0]nos -> K+ K- (pi0 -> gamma gamma)]cc, [[B0]os -> K- K+ (pi0 -> gamma gamma)]cc}
#
from Configurables import Generation
Generation().EventType = 11102422
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_K+K-pi0=DecProdCut,sqDalitz.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
