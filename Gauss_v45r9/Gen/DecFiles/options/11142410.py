# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11142410.py generated: Fri, 27 Mar 2015 16:10:03
#
# Event Type: 11142410
#
# ASCII decay Descriptor: [ B0 -> (J/psi(1S) -> mu+ mu-) (K_S0 -> pi0 pi0) ]cc
#
from Configurables import Generation
Generation().EventType = 11142410
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_JpsiKS,mmpi0pi0=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
