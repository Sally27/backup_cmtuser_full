# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/23163050.py generated: Fri, 27 Mar 2015 15:48:14
#
# Event Type: 23163050
#
# ASCII decay Descriptor: [D_s+ -> pi- K+ K+]cc
#
from Configurables import Generation
Generation().EventType = 23163050
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds+_pi-K+K+=phsp,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 431,-431 ]
