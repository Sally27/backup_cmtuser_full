# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/15164510.py generated: Fri, 27 Mar 2015 16:09:59
#
# Event Type: 15164510
#
# ASCII decay Descriptor: [Lambda_b0 -> (Sigma_c(2455)+ -> pi0 (Lambda_c+ -> Lambda0 pi+)) pi-]cc
#
from Configurables import Generation
Generation().EventType = 15164510
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Sigmacpipi,Lambdacpi0,Lambdapi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
