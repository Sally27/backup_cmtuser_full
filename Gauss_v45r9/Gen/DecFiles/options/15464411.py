# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/15464411.py generated: Fri, 27 Mar 2015 16:10:00
#
# Event Type: 15464411
#
# ASCII decay Descriptor: [Lambda_b0 -> (D*(2010)~0 -> (D~0 -> K+ pi-) {pi0, gamma}) p+ pi- ]cc
#
from Configurables import Generation
Generation().EventType = 15464411
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Dst0ppi,Kpi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
