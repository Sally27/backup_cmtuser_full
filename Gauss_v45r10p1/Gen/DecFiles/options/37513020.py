# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/37513020.py generated: Wed, 25 Jan 2017 15:25:21
#
# Event Type: 37513020
#
# ASCII decay Descriptor: [ K+ -> mu+ mu- mu+ nu_mu]cc
#
from Configurables import Generation
Generation().EventType = 37513020
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/K+_mumumunu=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 321,-321 ]
