# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/31503049.py generated: Fri, 27 Mar 2015 16:10:02
#
# Event Type: 31503049
#
# ASCII decay Descriptor: [tau- -> K- (phi(1020) -> K+ K-) nu_tau]cc
#
from Configurables import Generation
Generation().EventType = 31503049
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/tau_Kphinu,KK=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 15,-15 ]
