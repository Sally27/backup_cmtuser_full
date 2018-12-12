# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/21123011.py generated: Wed, 25 Jan 2017 15:25:16
#
# Event Type: 21123011
#
# ASCII decay Descriptor: [D+ -> pi- e+ e+]cc
#
from Configurables import Generation
Generation().EventType = 21123011
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D+_pi-ee=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 411,-411 ]
