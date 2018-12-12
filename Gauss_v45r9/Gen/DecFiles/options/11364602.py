# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11364602.py generated: Fri, 27 Mar 2015 16:10:02
#
# Event Type: 11364602
#
# ASCII decay Descriptor: {[[B0]nos -> (D*_s- -> {gamma (D_s- => (phi -> K+ K-) (rho- -> pi- pi0)), pi0 (D_s- => (phi -> K+ K-) (rho- -> pi- pi0))}) K+]cc, [[B0]os -> (D*_s+ -> {gamma (D_s+ => (phi -> K+ K-) (rho+ -> pi+ pi0)), pi0 (D_s+ => (phi -> K+ K-) (rho+ -> pi+ pi0))}) K-]cc}
#
from Configurables import Generation
Generation().EventType = 11364602
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_DsstK,phirho=SVV,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
