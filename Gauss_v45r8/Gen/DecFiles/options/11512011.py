# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11512011.py generated: Fri, 27 Mar 2015 15:48:08
#
# Event Type: 11512011
#
# ASCII decay Descriptor: [B0 => pi- nu_mu mu+]cc
#
from Configurables import Generation
Generation().EventType = 11512011
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_pimunu=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
