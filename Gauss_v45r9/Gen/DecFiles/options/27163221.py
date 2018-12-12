# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/27163221.py generated: Fri, 27 Mar 2015 16:10:07
#
# Event Type: 27163221
#
# ASCII decay Descriptor: [D*_s+ -> (D_s+ -> K+ K- pi+) gamma ]cc
#
from Configurables import Generation
Generation().EventType = 27163221
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Dsst_Dsgamma,KKpi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 433,-433 ]
