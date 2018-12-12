# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/31113013.py generated: Fri, 27 Mar 2015 15:48:11
#
# Event Type: 31113013
#
# ASCII decay Descriptor: [tau- -> mu- mu+ e-]cc
#
from Configurables import Generation
Generation().EventType = 31113013
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/tau_mumue=OS,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 15,-15 ]
