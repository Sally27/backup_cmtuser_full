# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/21101400.py generated: Fri, 27 Mar 2015 16:10:18
#
# Event Type: 21101400
#
# ASCII decay Descriptor: [D- -> pi- ( pi0 -> gamma gamma )]cc
#
from Configurables import Generation
Generation().EventType = 21101400
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D+_pi+pi0,gg=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 411,-411 ]
