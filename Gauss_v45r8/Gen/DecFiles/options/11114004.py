# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11114004.py generated: Fri, 27 Mar 2015 15:48:05
#
# Event Type: 11114004
#
# ASCII decay Descriptor: {[[B0]nos -> mu+ mu- (K*(892)0 -> K+ pi-)]cc, [[B0]os -> mu- mu+ (K*(892)~0 -> K- pi+)]cc}
#
from Configurables import Generation
Generation().EventType = 11114004
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Kstmumu=MS,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
