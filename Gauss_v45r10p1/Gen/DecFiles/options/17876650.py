# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/17876650.py generated: Wed, 25 Jan 2017 15:25:33
#
# Event Type: 17876650
#
# ASCII decay Descriptor: [B_s2*0 -> K- (B+ -> D~0 X mu+ nu_mu)]cc
#
from Configurables import Generation
Generation().EventType = 17876650
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bs1_BstK,D0XMuNu,D0=cocktail,mm=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 10533,-10533 ]
