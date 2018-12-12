# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11122200.py generated: Fri, 27 Mar 2015 15:47:58
#
# Event Type: 11122200
#
# ASCII decay Descriptor: [B_d0 -> gamma e+ e-]cc
#
from Configurables import Generation
Generation().EventType = 11122200
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_gammaee=MNT,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
