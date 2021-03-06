# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/23103240.py generated: Fri, 27 Mar 2015 16:10:12
#
# Event Type: 23103240
#
# ASCII decay Descriptor: [D_s+ -> ( eta -> pi+ pi- gamma) K+]cc
#
from Configurables import Generation
Generation().EventType = 23103240
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds+_etaK,pipigamma=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 431,-431 ]
