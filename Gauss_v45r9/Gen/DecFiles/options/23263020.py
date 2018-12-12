# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/23263020.py generated: Fri, 27 Mar 2015 16:10:16
#
# Event Type: 23263020
#
# ASCII decay Descriptor: [D_s+ -> K- K+ pi+]cc
#
from Configurables import Generation
Generation().EventType = 23263020
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds+_K-K+pi+=res,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 431,-431 ]
