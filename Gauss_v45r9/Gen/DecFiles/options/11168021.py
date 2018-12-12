# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11168021.py generated: Fri, 27 Mar 2015 16:10:04
#
# Event Type: 11168021
#
# ASCII decay Descriptor: {[[B0]nos -> (D*(2010)- -> pi- (D~0 -> K+ pi- pi+ pi-)) (a_1(1260)+ -> pi+ (rho(770)0 -> pi+ pi-))]cc, [[B0]os -> (D*(2010)+ -> pi+ (D0 -> K- pi+  pi- pi+)) (a_1(1260)- -> pi- (rho(770)0 -> pi- pi+))]cc}
#
from Configurables import Generation
Generation().EventType = 11168021
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dst-a1+,D0pi,K3pi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
