# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/34124000.py generated: Fri, 27 Mar 2015 16:10:07
#
# Event Type: 34124000
#
# ASCII decay Descriptor: K_S0 -> e+ e- e+ e-
#
from Configurables import Generation
Generation().EventType = 34124000
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/KS_4e.dec"
Generation().SignalPlain.CutTool = ""
Generation().SignalPlain.SignalPIDList = [ 310 ]
