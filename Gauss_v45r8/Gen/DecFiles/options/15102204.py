# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/15102204.py generated: Fri, 27 Mar 2015 15:48:11
#
# Event Type: 15102204
#
# ASCII decay Descriptor: [Lambda_b0 -> (Lambda(1810)0 -> p+ K-) gamma]cc
#
from Configurables import Generation
Generation().EventType = 15102204
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_gammaLambda1810,pK=phsp.dec"
Generation().SignalPlain.CutTool = "LHCbAcceptance"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
