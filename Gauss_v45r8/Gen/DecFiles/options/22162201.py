# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/22162201.py generated: Fri, 27 Mar 2015 15:48:04
#
# Event Type: 22162201
#
# ASCII decay Descriptor: [D0 -> (phi(1020) -> K+ K-) (gamma)]cc
#
from Configurables import Generation
Generation().EventType = 22162201
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D0_phigamma,KK=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 421,-421 ]
