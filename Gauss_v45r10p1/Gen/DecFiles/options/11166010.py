# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11166010.py generated: Wed, 25 Jan 2017 15:25:30
#
# Event Type: 11166010
#
# ASCII decay Descriptor: {[[B0]nos -> (D- => K+ pi- pi-) (a_1(1260)+ -> pi+ (rho(770)0 -> pi+ pi-))]cc, [[B0]os -> (D+ => K- pi+ pi+) (a_1(1260)- -> pi- (rho(770)0 -> pi- pi+))]cc}
#
from Configurables import Generation
Generation().EventType = 11166010
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D-a1+,D0pi-.dec"
Generation().SignalRepeatedHadronization.CutTool = "LHCbAcceptance"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
