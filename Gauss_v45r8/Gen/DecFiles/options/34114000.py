# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/34114000.py generated: Fri, 27 Mar 2015 15:48:14
#
# Event Type: 34114000
#
# ASCII decay Descriptor: K_S0 -> pi+ pi- mu+ mu-
#
from Configurables import Generation
Generation().EventType = 34114000
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/KS_pipimumu.dec"
Generation().SignalPlain.CutTool = ""
Generation().SignalPlain.SignalPIDList = [ 310 ]
