# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/15104541.py generated: Fri, 27 Mar 2015 15:48:06
#
# Event Type: 15104541
#
# ASCII decay Descriptor: [Lambda_b0  -> (Lambda0 -> p+ pi-) (rho+ -> pi0 pi+) K-]cc
#
from Configurables import Generation
Generation().EventType = 15104541
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Lambdarho+K-,pi+pi0=phsp,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
