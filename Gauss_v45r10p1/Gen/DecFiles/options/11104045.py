# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11104045.py generated: Wed, 25 Jan 2017 15:25:21
#
# Event Type: 11104045
#
# ASCII decay Descriptor: {[[B0]nos -> (a_1(1260)+ -> pi+ (rho(770)0 -> pi+ pi-)) pi- ]cc, [[B0]os -> (a_1(1260)- -> pi- (rho(770)0 -> pi- pi+)) pi+ ]cc}
#
from Configurables import Generation
Generation().EventType = 11104045
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_a1+pi-,rho0pi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LHCbAcceptance"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
