# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/16104144.py generated: Fri, 27 Mar 2015 15:48:03
#
# Event Type: 16104144
#
# ASCII decay Descriptor: [Xi_b0  -> p+ K- (KS0 -> pi+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 16104144
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xib0_KSpK=sqDalitz,pKref,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5232,-5232 ]
