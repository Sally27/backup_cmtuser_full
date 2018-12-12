# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/35103100.py generated: Fri, 27 Mar 2015 15:48:02
#
# Event Type: 35103100
#
# ASCII decay Descriptor: [Xi- -> (Lambda0 -> p+ pi-) pi-]cc
#
from Configurables import Generation
Generation().EventType = 35103100
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xi_LambdaPi.dec"
Generation().SignalPlain.CutTool = "LHCbAcceptance"
Generation().SignalPlain.SignalPIDList = [ 3312,-3312 ]
