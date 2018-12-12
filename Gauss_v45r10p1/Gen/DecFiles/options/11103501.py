# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11103501.py generated: Wed, 25 Jan 2017 15:25:27
#
# Event Type: 11103501
#
# ASCII decay Descriptor: {[B0-> (rho+ -> pi+ pi0) (K*(892)- -> (KS0 -> pi+ pi-) pi-)]cc, [B0-> (rho- -> pi- pi0) (K*(892)+ -> (KS0 -> pi+ pi-) pi+)]cc}
#
from Configurables import Generation
Generation().EventType = 11103501
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Kstrho,KSpi,pipi0=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
