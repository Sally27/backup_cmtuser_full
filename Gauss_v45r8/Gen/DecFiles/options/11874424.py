# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11874424.py generated: Fri, 27 Mar 2015 15:48:13
#
# Event Type: 11874424
#
# ASCII decay Descriptor: {[[B0]nos => nu_mu mu+ (D*(2010)- => (D~0 -> K+ K-) pi-)]cc, [[B0]os => anti_nu_mu mu- (D*(2010)+ => (D0 -> K- K+) pi+)]cc}
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/D0muInAcc.py" )
from Configurables import Generation
Generation().EventType = 11874424
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dstmunu,KK=cocktail,hqet,D0muInAcc,BRCorr1.dec"
Generation().SignalRepeatedHadronization.CutTool = "ListOfDaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
