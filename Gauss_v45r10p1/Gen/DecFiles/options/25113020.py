# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/25113020.py generated: Wed, 25 Jan 2017 15:25:16
#
# Event Type: 25113020
#
# ASCII decay Descriptor: [Lambda_c+ -> p+ (omega(782) -> mu- mu+)]cc
#
from Configurables import Generation
Generation().EventType = 25113020
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lc_pomega,mumu=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 4122,-4122 ]
