# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11104041.py generated: Fri, 27 Mar 2015 16:10:02
#
# Event Type: 11104041
#
# ASCII decay Descriptor: [B0-> (rho0 -> pi+pi-) (K*0-> K+pi-)]cc
#
from Configurables import Generation
Generation().EventType = 11104041
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Kst0rho0,K+pi-pi+pi-=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
