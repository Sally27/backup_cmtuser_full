# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11164631.py generated: Fri, 27 Mar 2015 15:48:06
#
# Event Type: 11164631
#
# ASCII decay Descriptor: {[[B0]nos -> (D_2*- -> (D*(2007)~0 -> {(D~0 -> K+ pi-) (pi0 -> gamma gamma), (D~0 -> K+ pi-) gamma} ) pi- ) pi+ ]cc, [[B0]os -> (D_2*- -> (D*(2007)0 -> {(D0 -> K- pi+) (pi0 -> gamma gamma), (D0 -> K- pi+) gamma} ) pi+ ) pi- ]cc}
#
from Configurables import Generation
Generation().EventType = 11164631
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D2stpi,Dst0pi,D0=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
