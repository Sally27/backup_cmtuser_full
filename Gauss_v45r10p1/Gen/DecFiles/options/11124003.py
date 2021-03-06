# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11124003.py generated: Wed, 25 Jan 2017 15:25:14
#
# Event Type: 11124003
#
# ASCII decay Descriptor: {[[B0]nos -> e+ e- (K*(892)0 -> K+ pi-)]cc, [[B0]os -> e- e+ (K*(892)~0 -> K- pi+)]cc}
#
from Configurables import Generation
Generation().EventType = 11124003
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Kstee,phsp=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
