# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/15104230.py generated: Wed, 25 Jan 2017 15:25:28
#
# Event Type: 15104230
#
# ASCII decay Descriptor: [Lambda_b0 -> pi- (eta' -> (rho0 -> pi+ pi-) gamma) p+]cc
#
from Configurables import Generation
Generation().EventType = 15104230
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_ppietap,rhogamma=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
