# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/21103110.py generated: Fri, 27 Mar 2015 16:10:15
#
# Event Type: 21103110
#
# ASCII decay Descriptor: [D+ -> (KS0 -> pi+ pi-) K+]cc
#
from Configurables import Generation
Generation().EventType = 21103110
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D+_KsK+=phsp,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 411,-411 ]
