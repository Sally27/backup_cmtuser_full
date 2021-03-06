# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/15264010.py generated: Wed, 25 Jan 2017 15:25:18
#
# Event Type: 15264010
#
# ASCII decay Descriptor: [Lambda_b0 -> (Lambda_c+ -> p K+ pi-) pi-]cc
#
from Configurables import Generation
Generation().EventType = 15264010
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Lambdacpi,pKpi.dec"
Generation().SignalPlain.CutTool = ""
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
