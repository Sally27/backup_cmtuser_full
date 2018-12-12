# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/15164051.py generated: Fri, 27 Mar 2015 15:48:09
#
# Event Type: 15164051
#
# ASCII decay Descriptor: [Lambda_b0 -> (D0 -> pi- pi+) p+ pi- ]cc
#
from Configurables import Generation
Generation().EventType = 15164051
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_D0ppi,pipi=sqDalitz,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
