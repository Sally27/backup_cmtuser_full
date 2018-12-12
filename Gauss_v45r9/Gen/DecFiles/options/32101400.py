# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/32101400.py generated: Fri, 27 Mar 2015 16:10:04
#
# Event Type: 32101400
#
# ASCII decay Descriptor: [Sigma+ => p+ pi0]cc
#
from Configurables import Generation
Generation().EventType = 32101400
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Sigma+_ppi0=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 3222,-3222 ]
