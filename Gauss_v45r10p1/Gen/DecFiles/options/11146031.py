# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11146031.py generated: Wed, 25 Jan 2017 15:25:32
#
# Event Type: 11146031
#
# ASCII decay Descriptor: [B0 -> (J/psi(1S) -> mu+ mu-)  (K*0 -> K+ pi-) (phi -> K+ K-)]cc
#
from Configurables import Generation
Generation().EventType = 11146031
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_JpsiphiKst,KKmumuKpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
