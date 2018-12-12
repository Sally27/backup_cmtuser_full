# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11104052.py generated: Fri, 27 Mar 2015 15:47:58
#
# Event Type: 11104052
#
# ASCII decay Descriptor: [B0 -> (rho(770)0 -> pi+ pi-) (rho(770)0 -> pi+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 11104052
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_rho0rho0=DecProdCut,Transverse.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
