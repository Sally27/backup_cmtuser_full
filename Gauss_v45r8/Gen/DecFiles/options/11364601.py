# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11364601.py generated: Fri, 27 Mar 2015 15:48:01
#
# Event Type: 11364601
#
# ASCII decay Descriptor: {[[B0]nos -> (D*_s- -> {gamma (D_s- => (phi -> K+ K-) (rho- -> pi- pi0)), pi0 (D_s- => (phi -> K+ K-) (rho- -> pi- pi0))}) pi+]cc, [[B0]os -> (D*_s+ -> {gamma (D_s+ => (phi -> K+ K-) (rho+ -> pi+ pi0)), pi0 (D_s+ => (phi -> K+ K-) (rho+ -> pi+ pi0))}) pi-]cc}
#
from Configurables import Generation
Generation().EventType = 11364601
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dsstpi,phirho=SVV,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
