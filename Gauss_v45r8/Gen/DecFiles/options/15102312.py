# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/15102312.py generated: Fri, 27 Mar 2015 15:48:03
#
# Event Type: 15102312
#
# ASCII decay Descriptor: [Lambda_b0 -> (Lambda0 -> p+ pi-) (eta_prime -> rho0 gamma)]cc
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Hb2KSetap.py" )
from Configurables import Generation
Generation().EventType = 15102312
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_etapLambda,rhog=DecProdCut,tightCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCbAndWithDaughAndBCuts"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
