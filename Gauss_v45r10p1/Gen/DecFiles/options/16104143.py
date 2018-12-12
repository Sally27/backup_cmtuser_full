# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/16104143.py generated: Wed, 25 Jan 2017 15:25:20
#
# Event Type: 16104143
#
# ASCII decay Descriptor: [Xi_b0  -> p+ pi- (KS0 -> pi+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 16104143
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xib0_KSppi=sqDalitz,ppiref,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5232,-5232 ]
