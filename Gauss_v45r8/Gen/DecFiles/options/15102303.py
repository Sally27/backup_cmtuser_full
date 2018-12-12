# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/15102303.py generated: Fri, 27 Mar 2015 15:48:09
#
# Event Type: 15102303
#
# ASCII decay Descriptor: [Lambda_b0 -> (Lambda0 -> p+ pi-) gamma]cc
#
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.PolarizedLambdad = True
from Configurables import Generation
Generation().EventType = 15102303
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_gammaLambda=trpol.dec"
Generation().SignalPlain.CutTool = "LHCbAcceptance"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
