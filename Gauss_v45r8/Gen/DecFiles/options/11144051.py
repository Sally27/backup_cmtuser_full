# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11144051.py generated: Fri, 27 Mar 2015 15:47:58
#
# Event Type: 11144051
#
# ASCII decay Descriptor: {[[B0]nos -> (psi(2S) -> mu+ mu- {,gamma} {,gamma}) K+ pi-]cc, [[B0]os -> (psi(2S) -> mu+ mu- {,gamma} {,gamma}) K- pi+]cc}
#
from Configurables import Generation
Generation().EventType = 11144051
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_psi2SKpi,mm=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
