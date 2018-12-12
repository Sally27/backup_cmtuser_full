# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/39312000.py generated: Wed, 25 Jan 2017 15:25:28
#
# Event Type: 39312000
#
# ASCII decay Descriptor: [phi(1020) => e+ mu-]CC
#
from Configurables import Generation
Generation().EventType = 39312000
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_phi,emu=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 333 ]
