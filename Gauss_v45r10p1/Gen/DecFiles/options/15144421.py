# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/15144421.py generated: Wed, 25 Jan 2017 15:25:36
#
# Event Type: 15144421
#
# ASCII decay Descriptor: [Lambda_b0 -> p+ K- (J/psi(1S) -> mu+ mu-) (pi0 -> gamma gamma) ]cc
#
from Configurables import Generation
Generation().EventType = 15144421
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_JpsipKpi0,mm=phsp,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
