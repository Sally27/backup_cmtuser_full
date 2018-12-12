# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11168102.py generated: Wed, 25 Jan 2017 15:25:30
#
# Event Type: 11168102
#
# ASCII decay Descriptor: [B0 -> (D*(2010)- -> (D~0 -> (K_S0 -> pi+ pi-) pi+ pi-) pi- ) (K*(892)+ -> (K_S0 -> pi+ pi-) pi+) ]cc
#
from Configurables import Generation
Generation().EventType = 11168102
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_DstKst,D0pi,KSpipi,KSpi=DecProdCut,HELAMP100.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
