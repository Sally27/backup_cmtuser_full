# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11102402.py generated: Fri, 27 Mar 2015 16:10:03
#
# Event Type: 11102402
#
# ASCII decay Descriptor: [B0 => pi+ pi- (pi0 -> gamma gamma)]cc
#
from Configurables import Generation
Generation().EventType = 11102402
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_pipipi=CPV,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
