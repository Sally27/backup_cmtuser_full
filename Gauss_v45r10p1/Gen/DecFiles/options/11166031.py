# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11166031.py generated: Wed, 25 Jan 2017 15:25:34
#
# Event Type: 11166031
#
# ASCII decay Descriptor: {[[B0]nos -> (D*(2010)- -> pi- (D~0 -> K+ pi-)) (K_1(1270)+ -> K+ (rho(770)0 -> pi+ pi-))]cc, [[B0]os -> (D*(2010)+ -> pi+ (D0 -> K- pi+)) (K_1(1270)- -> K- (rho(770)0 -> pi- pi+))]cc}
#
from Configurables import Generation
Generation().EventType = 11166031
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dst-K1+,D0pi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
