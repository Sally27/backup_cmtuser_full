# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11314056.py generated: Wed, 25 Jan 2017 15:25:17
#
# Event Type: 11314056
#
# ASCII decay Descriptor: {[B0 -> (omega(782) -> pi+ pi-) e+ mu-]cc,[B0 -> (omega(782) -> pi+ pi-) e- mu+]cc}
#
from Configurables import Generation
Generation().EventType = 11314056
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_omegaemu,pipi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
