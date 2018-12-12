# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/26104080.py generated: Fri, 27 Mar 2015 15:48:00
#
# Event Type: 26104080
#
# ASCII decay Descriptor: {[Xi_c0 -> p+ K- K- pi+]cc}
#
from Configurables import Generation
Generation().EventType = 26104080
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xic0_pKKpi=phsp,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 4132,-4132 ]
