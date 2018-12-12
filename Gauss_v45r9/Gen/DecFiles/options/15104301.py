# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/15104301.py generated: Fri, 27 Mar 2015 16:09:58
#
# Event Type: 15104301
#
# ASCII decay Descriptor: [Lambda_b0 -> (Lambda0 -> p+ pi-) (eta_prime -> pi+ pi- gamma)]cc
#
from Configurables import Generation
Generation().EventType = 15104301
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_etapLambda,pi+pi-g=DecProdCut,PHSP.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
