# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/23113002.py generated: Fri, 27 Mar 2015 16:10:14
#
# Event Type: 23113002
#
# ASCII decay Descriptor: [D_s+ => ( phi(1020) => mu+ mu- ) K+]cc
#
from Configurables import Generation
Generation().EventType = 23113002
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds_phiK,mm=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 431,-431 ]
