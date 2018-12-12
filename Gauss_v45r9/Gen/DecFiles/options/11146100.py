# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11146100.py generated: Fri, 27 Mar 2015 16:10:02
#
# Event Type: 11146100
#
# ASCII decay Descriptor: [B0 -> KS (psi(2S) -> (J/psi(1S) -> mu+ mu- {,gamma} {,gamma}) pi+pi-)]cc
#
from Configurables import Generation
Generation().EventType = 11146100
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_psi2SKS,Jpsipipi,mm=CPV,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
