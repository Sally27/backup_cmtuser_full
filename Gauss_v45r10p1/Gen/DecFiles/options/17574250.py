# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/17574250.py generated: Wed, 25 Jan 2017 15:25:25
#
# Event Type: 17574250
#
# ASCII decay Descriptor: [B_s1(L)0 -> K- (B*+ ->(B+ -> D~0 mu+ nu_mu) gamma)]cc
#
from Configurables import Generation
Generation().EventType = 17574250
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bs1_BstK,D0MuNu,mm=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 10533,-10533 ]
