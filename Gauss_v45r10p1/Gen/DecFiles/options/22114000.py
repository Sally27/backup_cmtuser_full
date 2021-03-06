# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/22114000.py generated: Wed, 25 Jan 2017 15:25:28
#
# Event Type: 22114000
#
# ASCII decay Descriptor: [D0 -> K+ K- mu+ mu-]cc
#
from Configurables import Generation
Generation().EventType = 22114000
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D0_KKmumu=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 421,-421 ]
