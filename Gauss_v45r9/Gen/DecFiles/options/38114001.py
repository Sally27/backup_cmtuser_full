# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/38114001.py generated: Fri, 27 Mar 2015 16:10:04
#
# Event Type: 38114001
#
# ASCII decay Descriptor: K_L0 -> mu+ mu- mu+ mu-
#
from Configurables import Generation
Generation().EventType = 38114001
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/KL_4mu=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 130 ]
