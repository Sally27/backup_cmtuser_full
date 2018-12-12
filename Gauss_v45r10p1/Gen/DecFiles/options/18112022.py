# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/18112022.py generated: Wed, 25 Jan 2017 15:25:25
#
# Event Type: 18112022
#
# ASCII decay Descriptor: Upsilon(3S) -> mu+ mu- {,gamma} {,gamma}
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Upsilon3S.py" )
from Configurables import Generation
Generation().EventType = 18112022
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_Upsilon3S,mm=NoCut.dec"
Generation().SignalPlain.CutTool = ""
