# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/36000000.py generated: Fri, 27 Mar 2015 16:10:00
#
# Event Type: 36000000
#
# ASCII decay Descriptor: pp => [<Omega->]cc ...
#
from Configurables import Generation
Generation().EventType = 36000000
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_Omega3334.dec"
Generation().SignalPlain.CutTool = "LHCbAcceptance"
Generation().SignalPlain.SignalPIDList = [ 3334,-3334 ]
