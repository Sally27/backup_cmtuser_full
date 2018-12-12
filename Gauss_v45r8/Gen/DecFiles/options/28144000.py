# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/28144000.py generated: Fri, 27 Mar 2015 15:48:09
#
# Event Type: 28144000
#
# ASCII decay Descriptor: psi(2S) -> (J/psi(1S) -> mu+ mu- {,gamma} {,gamma}) pi+ pi-
#
from Configurables import Generation
Generation().EventType = 28144000
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_psi2S,Jpsipipi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 100443 ]
