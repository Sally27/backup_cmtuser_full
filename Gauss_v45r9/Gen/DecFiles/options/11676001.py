# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11676001.py generated: Fri, 27 Mar 2015 16:10:16
#
# Event Type: 11676001
#
# ASCII decay Descriptor: {[[B0]nos->nu_mu mu+ (D*(2010)- -> pi- (D~0 => K+ pi- pi+ pi-))]cc,[[B0]os -> anti_nu_mu mu- (D*(2010)+ -> pi+ (D0 => K- pi+ pi- pi+))]cc}
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/D0muInAcc.py" )
from Configurables import Generation
Generation().EventType = 11676001
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dstmunu,Kpipipi=hqet,MINT,D0muInAcc.dec"
Generation().SignalRepeatedHadronization.CutTool = "ListOfDaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
