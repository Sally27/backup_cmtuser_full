# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/15164101.py generated: Fri, 27 Mar 2015 16:10:05
#
# Event Type: 15164101
#
# ASCII decay Descriptor: [Lambda_b0 -> ( Xi_c+ -> ( Lambda0 -> p+ pi- ) pi+ ) pi-]cc
#
from Configurables import Generation
Generation().EventType = 15164101
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Xicpi,Lambdapi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
