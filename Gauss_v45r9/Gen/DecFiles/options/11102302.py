# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11102302.py generated: Fri, 27 Mar 2015 16:10:07
#
# Event Type: 11102302
#
# ASCII decay Descriptor: [B0 -> (eta_prime -> rho0 gamma) (KS0 -> pi+ pi-)]cc
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Hb2KSetap.py" )
from Configurables import Generation
Generation().EventType = 11102302
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_etapKs,rhogamma=DecProdCut,tightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCbAndWithDaughAndBCuts"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
