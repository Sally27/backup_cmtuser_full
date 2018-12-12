# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/28142001.py generated: Fri, 27 Mar 2015 16:10:17
#
# Event Type: 28142001
#
# ASCII decay Descriptor: psi(2S) -> mu+ mu- {,gamma} {,gamma}
#
from Configurables import Generation
Generation().EventType = 28142001
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_psi2S,mm=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 100443 ]
