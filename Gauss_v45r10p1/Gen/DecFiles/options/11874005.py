# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11874005.py generated: Wed, 25 Jan 2017 15:25:23
#
# Event Type: 11874005
#
# ASCII decay Descriptor: {[[B0]nos => nu_mu mu+ (D*(2010)- -> pi- (D~0 -> K+ pi-))]cc, [[B0]os => anti_nu_mu mu- (D*(2010)+ -> pi+ (D0 -> K- pi+))]cc}
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/D0muInAcc.py" )
from Configurables import Generation
Generation().EventType = 11874005
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dstmunu_BKG=Kpi,cocktail,hqet,D0muInAcc,BRcorr2.dec"
Generation().SignalRepeatedHadronization.CutTool = "ListOfDaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
