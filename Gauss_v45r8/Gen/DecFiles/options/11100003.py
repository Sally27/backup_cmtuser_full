# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11100003.py generated: Fri, 27 Mar 2015 15:48:01
#
# Event Type: 11100003
#
# ASCII decay Descriptor: [B0-> Ks pi+ pi- gamma]cc
#
from Configurables import Generation
Generation().EventType = 11100003
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Kspi+pi-gamma=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
