# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/15174011.py generated: Fri, 27 Mar 2015 16:10:06
#
# Event Type: 15174011
#
# ASCII decay Descriptor: [Lambda_b0 -> D+(-> K- pi+ pi+) mu-]cc
#
from Configurables import Generation
Generation().EventType = 15174011
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_D+mu,Kpipi=phsp,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
