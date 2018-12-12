# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11202601.py generated: Fri, 27 Mar 2015 15:48:05
#
# Event Type: 11202601
#
# ASCII decay Descriptor: [ B0 -> (K_1(1270)0 -> (X0 ->  K+ pi- pi0)) gamma ]cc
#
from Configurables import Generation
Generation().EventType = 11202601
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_K1gamma,Kpipi0=mK1270,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
