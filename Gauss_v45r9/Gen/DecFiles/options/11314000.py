# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11314000.py generated: Fri, 27 Mar 2015 16:10:13
#
# Event Type: 11314000
#
# ASCII decay Descriptor: {[[B0]nos -> mu+ e- (K*(892)0 -> K+ pi-)]cc, [[B0]nos -> e+ mu- (K*(892)0 -> K+ pi-)]cc, [[B0]os -> mu- e+ (K*(892)~0 -> K- pi+)]cc, [[B0]os -> e- mu+ (K*(892)~0 -> K- pi+)]cc}
#
from Configurables import Generation
Generation().EventType = 11314000
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Kstemu=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
