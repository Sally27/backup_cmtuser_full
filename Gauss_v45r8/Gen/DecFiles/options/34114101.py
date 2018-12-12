# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/34114101.py generated: Fri, 27 Mar 2015 15:48:08
#
# Event Type: 34114101
#
# ASCII decay Descriptor: K_S0 -> mu+ mu- mu+ mu-
#
from Configurables import Generation
Generation().EventType = 34114101
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/KS_4mu=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 310 ]
