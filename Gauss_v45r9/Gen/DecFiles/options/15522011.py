# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/15522011.py generated: Fri, 27 Mar 2015 16:10:03
#
# Event Type: 15522011
#
# ASCII decay Descriptor: [Lambda_b0 -> p+ e- anti-nu_e]cc
#
from Configurables import Generation
Generation().EventType = 15522011
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_penu=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
