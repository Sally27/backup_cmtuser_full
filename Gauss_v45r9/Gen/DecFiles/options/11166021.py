# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11166021.py generated: Fri, 27 Mar 2015 16:09:59
#
# Event Type: 11166021
#
# ASCII decay Descriptor: {[[B0]nos -> (D*(2010)- -> pi- (D~0 -> K+ pi-)) (a_1(1260)+ -> pi+ (rho(770)0 -> pi+ pi-))]cc, [[B0]os -> (D*(2010)+ -> pi+ (D0 -> K- pi+)) (a_1(1260)- -> pi- (rho(770)0 -> pi- pi+))]cc}
#
from Configurables import Generation
Generation().EventType = 11166021
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dst-a1+,D0pi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
