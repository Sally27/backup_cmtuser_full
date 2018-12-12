# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/18112012.py generated: Wed, 25 Jan 2017 15:25:14
#
# Event Type: 18112012
#
# ASCII decay Descriptor: Upsilon(2S) -> mu+ mu- {,gamma} {,gamma}
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Upsilon2S.py" )
from Configurables import Generation
Generation().EventType = 18112012
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_Upsilon2S,mm=NoCut.dec"
Generation().SignalPlain.CutTool = ""
