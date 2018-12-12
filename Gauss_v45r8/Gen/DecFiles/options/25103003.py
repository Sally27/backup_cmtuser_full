# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/25103003.py generated: Fri, 27 Mar 2015 15:48:02
#
# Event Type: 25103003
#
# ASCII decay Descriptor: [Lambda_c+ -> p+ pi- K+]cc
#
from Configurables import Generation
Generation().EventType = 25103003
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lc_ppiK=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 4122,-4122 ]
