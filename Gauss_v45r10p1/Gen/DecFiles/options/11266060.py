# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11266060.py generated: Wed, 25 Jan 2017 15:25:20
#
# Event Type: 11266060
#
# ASCII decay Descriptor: {[[B0]nos -> (D~0 -> K+ pi- pi+ pi-)(rho(770)0 -> pi+ pi-)]cc, [[B0]os -> (D0 -> K- pi+ pi- pi+) (rho(770)0 -> pi+ pi-)]cc}
#
from Configurables import Generation
Generation().EventType = 11266060
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D0rho0,K3pi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
