# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11104051.py generated: Fri, 27 Mar 2015 16:10:13
#
# Event Type: 11104051
#
# ASCII decay Descriptor: [B0 -> (rho(770)0 -> pi+ pi-) (rho(770)0 -> pi+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 11104051
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_rho0rho0=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
