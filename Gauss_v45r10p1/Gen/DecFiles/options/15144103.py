# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/15144103.py generated: Wed, 25 Jan 2017 15:25:14
#
# Event Type: 15144103
#
# ASCII decay Descriptor: [Lambda_b0 -> (Lambda0 -> p+ pi-) (J/psi(1S) -> mu+ mu- {,gamma} {,gamma})]cc
#
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.PolarizedLambdad = True
from Configurables import Generation
Generation().EventType = 15144103
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_JpsiLambda,mm=phsp,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
