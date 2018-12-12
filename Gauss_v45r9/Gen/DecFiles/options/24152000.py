# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/24152000.py generated: Fri, 27 Mar 2015 16:10:03
#
# Event Type: 24152000
#
# ASCII decay Descriptor: J/psi(1S) -> e+ e- {,gamma} {,gamma}
#
from Configurables import Generation
Generation().EventType = 24152000
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_Jpsi,ee=NoCut.dec"
Generation().SignalPlain.CutTool = ""
Generation().SignalPlain.SignalPIDList = [ 443 ]
