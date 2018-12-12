# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/15244211.py generated: Wed, 25 Jan 2017 15:25:33
#
# Event Type: 15244211
#
# ASCII decay Descriptor: [Lambda_b0 -> ( psi(2S) -> ( [chi_c0(1P) , chi_c1(1P) , chi_c2(1P)] -> (J/psi -> mu+ mu- ) gamma ) gamma ) p+ K- ]cc
#
from Configurables import Generation
Generation().EventType = 15244211
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_psi2SpK,chicg,Jpsig,mm=PHSP,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
