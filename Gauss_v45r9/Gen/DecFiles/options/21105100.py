# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/21105100.py generated: Fri, 27 Mar 2015 16:10:01
#
# Event Type: 21105100
#
# ASCII decay Descriptor: [D+ -> (KS0 -> pi+ pi-) pi+ pi- pi+]cc
#
from Configurables import Generation
Generation().EventType = 21105100
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D+_Kspi+pi-pi+=phsp,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 411,-411 ]
