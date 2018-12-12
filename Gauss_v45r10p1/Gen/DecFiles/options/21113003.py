# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/21113003.py generated: Wed, 25 Jan 2017 15:25:35
#
# Event Type: 21113003
#
# ASCII decay Descriptor: [D+ -> K- mu+ mu+]cc
#
from Configurables import Generation
Generation().EventType = 21113003
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D+_K-mu+mu+=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 411,-411 ]
