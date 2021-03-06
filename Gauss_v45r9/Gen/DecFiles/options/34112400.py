# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/34112400.py generated: Fri, 27 Mar 2015 16:10:15
#
# Event Type: 34112400
#
# ASCII decay Descriptor: K_S0 -> mu+ mu- pi0
#
from Configurables import Generation
Generation().EventType = 34112400
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/KS_mumupi0.dec"
Generation().SignalPlain.CutTool = ""
Generation().SignalPlain.SignalPIDList = [ 310 ]
