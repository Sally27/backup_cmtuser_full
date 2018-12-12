# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11164470.py generated: Wed, 25 Jan 2017 15:25:22
#
# Event Type: 11164470
#
# ASCII decay Descriptor: {[[B0]nos -> (D- -> K+ pi- pi-) (K*(892)+ -> K+ pi0)]cc, [[B0]os -> (D+ -> K- pi+ pi+) (K*(892)- -> K- pi0)]cc}
#
from Configurables import Generation
Generation().EventType = 11164470
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D-Kst+,Kpipi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]