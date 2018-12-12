# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11164042.py generated: Fri, 27 Mar 2015 16:10:11
#
# Event Type: 11164042
#
# ASCII decay Descriptor: {[[B0]nos => pi+ (D_2*- -> pi- (D~0 -> K+ pi-))]cc, [[B0]os => pi- (D_2*+ -> pi+ (D0 -> K- pi+))]cc}
#
from Configurables import Generation
Generation().EventType = 11164042
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D2stpi,D0pi,Kpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
