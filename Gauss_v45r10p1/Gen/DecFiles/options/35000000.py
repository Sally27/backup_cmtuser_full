# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/35000000.py generated: Wed, 25 Jan 2017 15:25:34
#
# Event Type: 35000000
#
# ASCII decay Descriptor: pp => [<Xi->]cc ...
#
from Configurables import Generation
Generation().EventType = 35000000
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_Xi3312.dec"
Generation().SignalPlain.CutTool = "LHCbAcceptance"
Generation().SignalPlain.SignalPIDList = [ 3312,-3312 ]
