# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/15146133.py generated: Wed, 25 Jan 2017 15:25:26
#
# Event Type: 15146133
#
# ASCII decay Descriptor: [Lambda_b0 ->  (J/psi(1S) -> mu+ mu-) (phi -> K+ K-) (Lambda0 -> p+ pi-) ]cc
#
from Configurables import Generation
Generation().EventType = 15146133
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_JpsiLambdaphi,mm=phsp,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
