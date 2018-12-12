# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/28142070.py generated: Fri, 27 Mar 2015 15:48:00
#
# Event Type: 28142070
#
# ASCII decay Descriptor: psi(3770) -> mu+ mu-
#
from Configurables import Generation
Generation().EventType = 28142070
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_psi3770,mm=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 30443 ]
