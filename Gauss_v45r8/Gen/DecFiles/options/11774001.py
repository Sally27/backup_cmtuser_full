# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11774001.py generated: Fri, 27 Mar 2015 15:48:11
#
# Event Type: 11774001
#
# ASCII decay Descriptor: {B~0 => (D_0*+ => (D_s+ => K+ K- pi+) anti-K0) anti-nu_mu mu-]cc}
#
from Configurables import Generation
Generation().EventType = 11774001
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dstp2400munu,DsKS0,KKpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
