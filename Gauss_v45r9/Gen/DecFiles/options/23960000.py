# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/23960000.py generated: Fri, 27 Mar 2015 16:10:17
#
# Event Type: 23960000
#
# ASCII decay Descriptor: [D_s+ -> ...]cc
#
from Configurables import Generation
Generation().EventType = 23960000
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds+,incl.dec"
Generation().SignalPlain.CutTool = "LHCbAcceptance"
Generation().SignalPlain.SignalPIDList = [ 431,-431 ]
