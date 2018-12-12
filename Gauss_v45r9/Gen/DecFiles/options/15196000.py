# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/15196000.py generated: Fri, 27 Mar 2015 16:10:18
#
# Event Type: 15196000
#
# ASCII decay Descriptor: [Lambda_b0 -> p+ D_s- D0]cc
#
from Configurables import Generation
Generation().EventType = 15196000
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_pDsD0,KKpi,Kpi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
