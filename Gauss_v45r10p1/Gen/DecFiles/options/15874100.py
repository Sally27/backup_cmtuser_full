# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/15874100.py generated: Wed, 25 Jan 2017 15:25:30
#
# Event Type: 15874100
#
# ASCII decay Descriptor: {[ Lambda_b0 => (Lambda_c+ -> (Lambda0 -> p+ pi-) pi+)  anti-nu_mu mu-]cc}
#
from Configurables import Generation
Generation().EventType = 15874100
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Lcmunu,LambdaPi=cocktail,DecProdCut.dec"
Generation().SignalPlain.CutTool = "LHCbAcceptance"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
