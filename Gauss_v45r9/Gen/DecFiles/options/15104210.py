# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/15104210.py generated: Fri, 27 Mar 2015 16:09:59
#
# Event Type: 15104210
#
# ASCII decay Descriptor: [Lambda_b0 -> (Lambda_c+ -> p+ KS0 (pi0 -> gamma gamma) ) pi-]cc
#
from Configurables import Generation
Generation().EventType = 15104210
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Lambdacpi,pKSpi0=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
