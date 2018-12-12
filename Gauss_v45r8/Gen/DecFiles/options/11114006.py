# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11114006.py generated: Fri, 27 Mar 2015 15:48:08
#
# Event Type: 11114006
#
# ASCII decay Descriptor: {[[B0]nos -> mu+ mu- (K*(892)0 -> K+ pi-)]cc, [[B0]os -> mu- mu+ (K*(892)~0 -> K- pi+)]cc}
#
from Configurables import Generation
Generation().EventType = 11114006
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenInPhSpDecay
ToolSvc().addTool( EvtGenInPhSpDecay )
ToolSvc().EvtGenInPhSpDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Kstmumu,phsp=DecProdCut,MomCut,Weight.dec"
Generation().DecayTool = "EvtGenInPhSpDecay"
Generation().SignalRepeatedHadronization.DecayTool = "EvtGenInPhSpDecay"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCbAndWithMinP"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
