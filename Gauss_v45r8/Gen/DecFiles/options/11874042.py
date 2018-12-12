# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11874042.py generated: Fri, 27 Mar 2015 15:48:14
#
# Event Type: 11874042
#
# ASCII decay Descriptor: {[[B0 => (D- => K+ pi- pi-) anti-nu_mu mu+]cc }
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/DmuInAcc.py" )
from Configurables import Generation
Generation().EventType = 11874042
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dmunu,K-pi+pi+=cocktail,hqet,BRCorr1,DmuInAcc.dec"
Generation().SignalRepeatedHadronization.CutTool = "ListOfDaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
