# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/15164001.py generated: Fri, 27 Mar 2015 15:48:15
#
# Event Type: 15164001
#
# ASCII decay Descriptor: [Lambda_b0 -> (Lambda_c+ -> p K+ pi-) pi-]cc
#
from Configurables import Generation
Generation().EventType = 15164001
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Lambdacpi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
