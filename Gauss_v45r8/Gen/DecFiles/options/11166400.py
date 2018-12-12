# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11166400.py generated: Fri, 27 Mar 2015 15:48:03
#
# Event Type: 11166400
#
# ASCII decay Descriptor: [B0 -> (D(*)- ->  (D- -> pi- pi+ pi- pi0) pi0 ) (tau+ ->  pi+  pi+  pi- anti-nu_tau ) nu_tau]cc
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/B2XTau.py" )
from Configurables import Generation
Generation().EventType = 11166400
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_DstTauNu,3pipi03pinu=DecProdCut,tightcut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCbAndWithDaughAndBCuts"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
