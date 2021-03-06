# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/36103100.py generated: Wed, 25 Jan 2017 15:25:26
#
# Event Type: 36103100
#
# ASCII decay Descriptor: [Omega- -> (Lambda0 -> p+ pi-) K-]cc
#
from Configurables import Generation
Generation().EventType = 36103100
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Omega_LambdaK+.dec"
Generation().SignalPlain.CutTool = "LHCbAcceptance"
Generation().SignalPlain.SignalPIDList = [ 3334,-3334 ]
