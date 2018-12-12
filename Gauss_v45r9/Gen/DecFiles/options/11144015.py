# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11144015.py generated: Fri, 27 Mar 2015 16:09:59
#
# Event Type: 11144015
#
# ASCII decay Descriptor: [B0 -> (J/psi(1S) -> mu+ mu-) (rho0 -> mu+ mu-)]cc
#
from Configurables import Generation
Generation().EventType = 11144015
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/B0_Jpsirho,4mu=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
