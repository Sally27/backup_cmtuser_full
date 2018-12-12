# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11144110.py generated: Fri, 27 Mar 2015 16:10:05
#
# Event Type: 11144110
#
# ASCII decay Descriptor: [B0 -> KS (psi(2S) ->  mu+ mu- {,gamma} {,gamma})]cc
#
from Configurables import Generation
Generation().EventType = 11144110
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_psi2SKS,mm=CPV,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
