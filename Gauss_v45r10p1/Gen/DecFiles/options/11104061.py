# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11104061.py generated: Wed, 25 Jan 2017 15:25:37
#
# Event Type: 11104061
#
# ASCII decay Descriptor: [B0 -> (rho(770)0 -> pi+ pi-) (rho(770)0 -> pi+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 11104061
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_rho0rho0=DecProdCut,eqPol.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
