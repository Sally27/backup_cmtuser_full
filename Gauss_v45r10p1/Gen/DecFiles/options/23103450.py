# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/23103450.py generated: Wed, 25 Jan 2017 15:25:16
#
# Event Type: 23103450
#
# ASCII decay Descriptor: [D_s+ -> ( eta' -> pi+ pi- ( eta -> gamma gamma ) ) pi+]cc
#
from Configurables import Generation
Generation().EventType = 23103450
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds+_etaprimepi,pipieta,gg=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 431,-431 ]
