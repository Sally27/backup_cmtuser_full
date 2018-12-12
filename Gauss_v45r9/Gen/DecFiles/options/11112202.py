# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11112202.py generated: Fri, 27 Mar 2015 16:10:08
#
# Event Type: 11112202
#
# ASCII decay Descriptor: [B_d0 -> gamma mu+ mu-]cc
#
from Configurables import Generation
Generation().EventType = 11112202
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_gammamumu=FSR,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
