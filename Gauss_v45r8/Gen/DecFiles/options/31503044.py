# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/31503044.py generated: Fri, 27 Mar 2015 15:48:00
#
# Event Type: 31503044
#
# ASCII decay Descriptor: [tau- -> pi- (phi(1020) -> K+ K-) nu_tau]cc
#
from Configurables import Generation
Generation().EventType = 31503044
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/tau_piphinu,KK=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 15,-15 ]
