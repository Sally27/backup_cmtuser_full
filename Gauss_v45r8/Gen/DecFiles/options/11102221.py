# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11102221.py generated: Fri, 27 Mar 2015 15:47:57
#
# Event Type: 11102221
#
# ASCII decay Descriptor: [B0 -> (rho0 -> pi+ pi-) gamma]cc
#
from Configurables import Generation
Generation().EventType = 11102221
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_rhogamma,pipi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
