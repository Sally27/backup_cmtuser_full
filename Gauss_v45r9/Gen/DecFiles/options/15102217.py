# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/15102217.py generated: Fri, 27 Mar 2015 16:10:02
#
# Event Type: 15102217
#
# ASCII decay Descriptor: [Lambda_b0 -> (Lambda(1800)0 -> p+ K-) gamma]cc
#
from Configurables import Generation
Generation().EventType = 15102217
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_gammaLambda1800,pK=phsp.dec"
Generation().SignalPlain.CutTool = "LHCbAcceptance"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
