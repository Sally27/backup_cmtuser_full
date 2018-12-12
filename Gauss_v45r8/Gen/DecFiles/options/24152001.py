# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/24152001.py generated: Fri, 27 Mar 2015 15:48:06
#
# Event Type: 24152001
#
# ASCII decay Descriptor: J/psi(1S) -> e+ e- {,gamma} {,gamma}
#
from Configurables import Generation
Generation().EventType = 24152001
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_Jpsi,ee=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 443 ]
