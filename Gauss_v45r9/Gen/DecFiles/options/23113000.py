# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/23113000.py generated: Fri, 27 Mar 2015 16:10:11
#
# Event Type: 23113000
#
# ASCII decay Descriptor: [Ds -> pi+ mu+ mu-]cc
#
from Configurables import Generation
Generation().EventType = 23113000
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds_pi+mumu=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 431,-431 ]
