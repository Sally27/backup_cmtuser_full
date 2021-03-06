# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/15364410.py generated: Wed, 25 Jan 2017 15:25:21
#
# Event Type: 15364410
#
# ASCII decay Descriptor: [Lambda_b0 -> (D*(2007)0 -> {(D0 -> pi- pi+) (pi0 -> gamma gamma), (D0 -> pi- pi+) gamma} ) p+ K- ]cc
#
from Configurables import Generation
Generation().EventType = 15364410
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Dst0pK,D0,pipi=sqDalitz,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
