# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/15266020.py generated: Fri, 27 Mar 2015 15:48:13
#
# Event Type: 15266020
#
# ASCII decay Descriptor: [Lb_b0 -> ((Lb_c(2593)+ -> (Lc+ -> p+ K- pi+)) pi+ pi-) pi-]cc
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/TracksInAccWithMinP.py" )
from Configurables import Generation
Generation().EventType = 15266020
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Lc2593pi,pKpi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCbAndWithMinP"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
