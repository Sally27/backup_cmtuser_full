# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/21265000.py generated: Fri, 27 Mar 2015 15:48:15
#
# Event Type: 21265000
#
# ASCII decay Descriptor: [D+ => K- pi- pi+ pi+ pi+]cc
#
from Configurables import Generation
Generation().EventType = 21265000
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D+_K-pi-pi+pi+pi+=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 411,-411 ]
