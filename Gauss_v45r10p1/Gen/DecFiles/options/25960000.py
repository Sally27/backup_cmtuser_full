# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/25960000.py generated: Wed, 25 Jan 2017 15:25:17
#
# Event Type: 25960000
#
# ASCII decay Descriptor: [Lambda_c+ -> ...]cc
#
from Configurables import Generation
Generation().EventType = 25960000
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lc,incl.dec"
Generation().SignalPlain.CutTool = "LHCbAcceptance"
Generation().SignalPlain.SignalPIDList = [ 4122,-4122 ]
