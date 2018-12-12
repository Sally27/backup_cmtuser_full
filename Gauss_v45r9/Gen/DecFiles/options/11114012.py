# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11114012.py generated: Fri, 27 Mar 2015 16:10:06
#
# Event Type: 11114012
#
# ASCII decay Descriptor: {[[B0]nos -> mu+ mu- K+ pi-]cc, [[B0]os -> mu- mu+ K- pi+]cc}
#
from Configurables import Generation
Generation().EventType = 11114012
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenInPhSpDecay
ToolSvc().addTool( EvtGenInPhSpDecay )
ToolSvc().EvtGenInPhSpDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Kpimumu,phsp=DecProdCut,MomCut,Weight.dec"
Generation().DecayTool = "EvtGenInPhSpDecay"
Generation().SignalRepeatedHadronization.DecayTool = "EvtGenInPhSpDecay"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCbAndWithMinP"
ToolSvc().EvtGenInPhSpDecay.MaxQ2Bins = 20
ToolSvc().EvtGenInPhSpDecay.MaxEvtGenCalls = 1500
ToolSvc().EvtGenInPhSpDecay.ParamFile = "KpiParam"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
