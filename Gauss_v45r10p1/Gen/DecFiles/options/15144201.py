# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/15144201.py generated: Wed, 25 Jan 2017 15:25:26
#
# Event Type: 15144201
#
# ASCII decay Descriptor: [Lambda_b0 -> ( chi_c2(1P) -> (J/psi -> mu+ mu- ) gamma ) p+ K- ]cc
#
from Configurables import Generation
Generation().EventType = 15144201
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_chic2pK,Jpsig,mm=PHSP,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
