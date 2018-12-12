# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/16104145.py generated: Fri, 27 Mar 2015 15:48:08
#
# Event Type: 16104145
#
# ASCII decay Descriptor: [Xi_b0  -> pi+ pi- ( Lambda0 -> p+ pi- )]cc
#
from Configurables import Generation
Generation().EventType = 16104145
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xib0_Lambdapipi,ppi=sqDalitz,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5232,-5232 ]
