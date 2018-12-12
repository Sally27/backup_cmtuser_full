# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/37103000.py generated: Fri, 27 Mar 2015 15:48:02
#
# Event Type: 37103000
#
# ASCII decay Descriptor: [ K+ => pi+ pi- pi+ ]cc
#
from Configurables import Generation
Generation().EventType = 37103000
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/K+_pipipi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 321,-321 ]
