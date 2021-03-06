# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/18112003.py generated: Fri, 27 Mar 2015 15:48:00
#
# Event Type: 18112003
#
# ASCII decay Descriptor: Upsilon(1S) -> mu+ mu- {,gamma} {,gamma}
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Upsilon1S.py" )
from Configurables import Generation
Generation().EventType = 18112003
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_Upsilon1S,mm=NoCut.dec"
Generation().SignalPlain.CutTool = ""
