# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/23103110.py generated: Wed, 25 Jan 2017 15:25:32
#
# Event Type: 23103110
#
# ASCII decay Descriptor: [Ds+ -> (KS0 -> pi+ pi-) K+]cc
#
from Configurables import Generation
Generation().EventType = 23103110
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds+_KsK+=phsp,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 431,-431 ]
