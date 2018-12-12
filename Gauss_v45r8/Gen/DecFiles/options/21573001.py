# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/21573001.py generated: Fri, 27 Mar 2015 15:47:58
#
# Event Type: 21573001
#
# ASCII decay Descriptor: [D+ -> anti-K*0(K- pi+)  mu+ nu_mu]cc
#
from Configurables import Generation
Generation().EventType = 21573001
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D+_Kst0munu=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 411,-411 ]
