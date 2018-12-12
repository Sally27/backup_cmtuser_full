# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11104431.py generated: Wed, 25 Jan 2017 15:25:22
#
# Event Type: 11104431
#
# ASCII decay Descriptor: [B0 -> (eta -> pi+ pi- pi0) (K*_2(1430)0 -> (K*(892)0 -> K+ pi-) pi0)]cc
#
from Configurables import Generation
Generation().EventType = 11104431
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_K2steta,pi+pi-pi0,Kstpi0=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
