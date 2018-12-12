# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/15442001.py generated: Fri, 27 Mar 2015 15:48:06
#
# Event Type: 15442001
#
# ASCII decay Descriptor: {[Lambda_b0 => (J/psi(1S) -> mu+ mu- {,gamma} {,gamma}) X]cc, [Lambda_b0 => (psi(2S) -> mu+ mu- {,gamma} {,gamma} X]cc}
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/CharmoniumInAcc.py" )
from Configurables import Generation
Generation().EventType = 15442001
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_JpsiX,mm=JpsiInAcc.dec"
Generation().SignalPlain.CutTool = "SelectedDaughterInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
