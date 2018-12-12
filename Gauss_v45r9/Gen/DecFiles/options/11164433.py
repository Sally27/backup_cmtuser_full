# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11164433.py generated: Fri, 27 Mar 2015 16:09:59
#
# Event Type: 11164433
#
# ASCII decay Descriptor: {[[B0]nos -> (D*(2007)~0 -> (D~0 -> pi+ pi-) (pi0 -> gamma gamma) ) (K*(892)~0 ->K- pi+) ]cc, [[B0]os -> (D*(2007)0 -> (D0 -> pi- pi+) (pi0 -> gamma gamma) ) (K*(892)0 ->K+ pi-) ]cc}
#
from Configurables import Generation
Generation().EventType = 11164433
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dst0Kst0,D0pi0,pipi=DecProdCut,HELAMP100.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
