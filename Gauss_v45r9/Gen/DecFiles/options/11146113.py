# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11146113.py generated: Fri, 27 Mar 2015 16:10:00
#
# Event Type: 11146113
#
# ASCII decay Descriptor: [B0 -> (J/psi(1S) -> mu+ mu-) (phi(1020) -> K+ K-) (K_S0 -> pi+ pi-)]cc
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/KKmumuInAcc.py" )
from Configurables import Generation
Generation().EventType = 11146113
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_JpsiphiKs,KKmumupipi=KKmumuInAcc.dec"
Generation().SignalRepeatedHadronization.CutTool = "ListOfDaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
