# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11314101.py generated: Wed, 25 Jan 2017 15:25:22
#
# Event Type: 11314101
#
# ASCII decay Descriptor: {[B0 -> (K_S0 -> pi+ pi-) e+ mu-]cc, [B0 -> (K_S0 -> pi+ pi-) e- mu+]cc}
#
from Configurables import Generation
Generation().EventType = 11314101
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_KSemu=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
