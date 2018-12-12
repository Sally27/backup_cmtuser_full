# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11314001.py generated: Wed, 25 Jan 2017 15:25:31
#
# Event Type: 11314001
#
# ASCII decay Descriptor: {[[B0]nos -> mu+ e- (K*(892)0 -> K+ pi-)]cc, [[B0]nos -> e+ mu- (K*(892)0 -> K+ pi-)]cc, [[B0]os -> mu- e+ (K*(892)~0 -> K- pi+)]cc, [[B0]os -> e- mu+ (K*(892)~0 -> K- pi+)]cc}
#
from Configurables import Generation
Generation().EventType = 11314001
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Kstemu=DecProdCut,PHSP.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
