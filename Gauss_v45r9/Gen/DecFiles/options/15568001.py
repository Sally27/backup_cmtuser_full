# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/15568001.py generated: Fri, 27 Mar 2015 16:10:08
#
# Event Type: 15568001
#
# ASCII decay Descriptor: [Lb_b0 => (Lb_c(2625)+ -> ((Lambda_c+ -> p+ K- pi+) pi+ pi-) tau- anti-nu_tau]cc
#
from Configurables import Generation
Generation().EventType = 15568001
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Lc2625TauNu,pKpi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
