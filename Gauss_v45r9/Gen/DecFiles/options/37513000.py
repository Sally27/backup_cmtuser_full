# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/37513000.py generated: Fri, 27 Mar 2015 16:10:08
#
# Event Type: 37513000
#
# ASCII decay Descriptor: [ K+ => pi+ pi- mu+ nu_mu ]cc
#
from Configurables import Generation
Generation().EventType = 37513000
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/K+_pipimunu=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 321,-321 ]
