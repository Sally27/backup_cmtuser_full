# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11146010.py generated: Wed, 25 Jan 2017 15:25:25
#
# Event Type: 11146010
#
# ASCII decay Descriptor: {[B0 -> (psi(2S) -> (J/psi(1S) -> mu+ mu-) pi+ pi-) K+ pi-]cc}
#
from Configurables import Generation
Generation().EventType = 11146010
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_psi2SKpi,Jpsipipi,mm=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
