# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11100001.py generated: Fri, 27 Mar 2015 16:10:19
#
# Event Type: 11100001
#
# ASCII decay Descriptor: [B0-> (rho0 -> pi+pi-) (K*0->(Ks->pi+pi-) pi0)]cc
#
from Configurables import Generation
Generation().EventType = 11100001
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Kst0rho0,KsPi0pi+pi-=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
