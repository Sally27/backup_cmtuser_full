# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/15266023.py generated: Fri, 27 Mar 2015 16:10:06
#
# Event Type: 15266023
#
# ASCII decay Descriptor: [Lambda_b0 -> (Sigma_c0 -> (Lc+ -> p+ K- pi+) pi-) pi+ pi-]cc
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/TracksInAccWithMinP.py" )
from Configurables import Generation
Generation().EventType = 15266023
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Sigmac0pipi,pKpi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCbAndWithMinP"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
