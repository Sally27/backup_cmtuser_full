# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/15154040.py generated: Wed, 25 Jan 2017 15:25:27
#
# Event Type: 15154040
#
# ASCII decay Descriptor: [Lambda_b0 -> (Lambda(1520)0 -> p+ K-) (J/psi -> e+ e-)]cc
#
from Configurables import Generation
Generation().EventType = 15154040
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Lambda1520Jpsi,ee=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
