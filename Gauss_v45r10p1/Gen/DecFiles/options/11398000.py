# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11398000.py generated: Wed, 25 Jan 2017 15:25:16
#
# Event Type: 11398000
#
# ASCII decay Descriptor: [B0 -> (D*(2010)- -> (anti-D0 -> K+ pi+ pi- pi-) pi-) ( (D+ -> pi+ K+ K-) || (D+ -> K- pi+ pi+ ) ) ]cc
#
from Configurables import Generation
Generation().EventType = 11398000
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_DstD,D0K3pi,Dkhh=CPV,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
