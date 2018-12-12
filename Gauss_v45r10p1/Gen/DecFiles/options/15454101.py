# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/15454101.py generated: Wed, 25 Jan 2017 15:25:33
#
# Event Type: 15454101
#
# ASCII decay Descriptor: {[Lambda_b0 => (J/psi(1S) -> e+ e- {,gamma} {,gamma}) X]cc, [Lambda_b0 => (psi(2S) -> e+ e- {,gamma} {,gamma} X]cc}
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/CharmoniumInAcc.py" )
from Configurables import Generation
Generation().EventType = 15454101
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_JpsiX,ee=JpsiInAcc.dec"
Generation().SignalPlain.CutTool = "SelectedDaughterInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
