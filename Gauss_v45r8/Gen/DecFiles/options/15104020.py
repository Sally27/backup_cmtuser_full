# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/15104020.py generated: Fri, 27 Mar 2015 15:48:09
#
# Event Type: 15104020
#
# ASCII decay Descriptor: [Lambda_b0 -> p+ K- (phi(1020) -> K+ K-)]cc
#
from Configurables import Generation
Generation().EventType = 15104020
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_pKphi,KK=phsp,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
