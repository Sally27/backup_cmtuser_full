# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/28136120.py generated: Fri, 27 Mar 2015 15:48:11
#
# Event Type: 28136120
#
# ASCII decay Descriptor: h_c -> (Xi- -> (Lambda -> p+ pi-) pi-) (Xi+ -> (Anti-Lambda -> p- pi+) pi+)
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/hc.py" )
from Configurables import Generation
Generation().EventType = 28136120
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/hc_XiXi,Lambdapi,ppi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "LHCbAcceptance"
Generation().SignalPlain.SignalPIDList = [ 10443 ]
