# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/15104101.py generated: Fri, 27 Mar 2015 16:10:04
#
# Event Type: 15104101
#
# ASCII decay Descriptor: [Lambda_b0  -> (KS0 -> pi+ pi-) p+ K-]cc
#
from Configurables import Generation
Generation().EventType = 15104101
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_KSpK=phsp,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
