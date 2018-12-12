# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/34112401.py generated: Fri, 27 Mar 2015 15:47:57
#
# Event Type: 34112401
#
# ASCII decay Descriptor: K_S0 -> mu+ mu- pi0
#
from Configurables import Generation
Generation().EventType = 34112401
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/KS_mumupi0=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 310 ]
