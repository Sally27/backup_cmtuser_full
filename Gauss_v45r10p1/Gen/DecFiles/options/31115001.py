# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/31115001.py generated: Wed, 25 Jan 2017 15:25:35
#
# Event Type: 31115001
#
# ASCII decay Descriptor: [tau- -> mu- mu+ mu- mu+ mu-]cc
#
from Configurables import Generation
Generation().EventType = 31115001
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/tau_5mu=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 15,-15 ]
