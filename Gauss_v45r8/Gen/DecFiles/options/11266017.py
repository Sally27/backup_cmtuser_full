# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11266017.py generated: Fri, 27 Mar 2015 15:48:14
#
# Event Type: 11266017
#
# ASCII decay Descriptor: {[[B0]nos -> (D_1(2420)~0 -> (D*(2010)- -> (D~0 -> K+ pi-) pi- ) pi+) pi+ pi-]cc, [[B0]os -> (D_1(2420)0 -> (D*(2010)+ -> (D0 -> K- pi+) pi+ ) pi-) pi- pi+]cc, [[B0]nos -> (D_1(H)~0 -> (D*(2010)- -> (D~0 -> K+ pi-) pi- ) pi+) pi+ pi-]cc, [[B0]os -> (D_1(H)0 -> (D*(2010)+ -> (D0 -> K- pi+) pi+ ) pi-) pi- pi+]cc}
#
from Configurables import Generation
Generation().EventType = 11266017
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D_10rho0,Dstpi,D0pi-=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
