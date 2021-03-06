# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/15104112.py generated: Fri, 27 Mar 2015 15:48:06
#
# Event Type: 15104112
#
# ASCII decay Descriptor: [Lambda_b0  -> (KS0 -> pi+ pi-) p+ pi-]cc
#
from Configurables import Generation
Generation().EventType = 15104112
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Ksppi=sqDalitz.dec"
Generation().SignalPlain.CutTool = "LHCbAcceptance"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
