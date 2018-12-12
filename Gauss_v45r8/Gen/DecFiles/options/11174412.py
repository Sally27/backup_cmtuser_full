# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11174412.py generated: Fri, 27 Mar 2015 15:48:12
#
# Event Type: 11174412
#
# ASCII decay Descriptor: [B0 -> (D*(2007)~0 -> (D~0 -> K+ pi-) pi0) mu+ mu-]cc
#
from Configurables import Generation
Generation().EventType = 11174412
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dst0mumu=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
