# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/39112000.py generated: Wed, 25 Jan 2017 15:25:26
#
# Event Type: 39112000
#
# ASCII decay Descriptor: [phi(1020) => mu+ mu-]CC
#
from Configurables import Generation
Generation().EventType = 39112000
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_phi,mumu=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 333 ]
