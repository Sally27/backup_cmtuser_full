# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/23163040.py generated: Fri, 27 Mar 2015 16:09:59
#
# Event Type: 23163040
#
# ASCII decay Descriptor: [D_s+ -> K- K+ K+]cc
#
from Configurables import Generation
Generation().EventType = 23163040
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds+_K-K+K+=phsp,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 431,-431 ]
