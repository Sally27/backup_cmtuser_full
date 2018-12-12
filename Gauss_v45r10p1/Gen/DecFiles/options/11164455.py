# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11164455.py generated: Wed, 25 Jan 2017 15:25:26
#
# Event Type: 11164455
#
# ASCII decay Descriptor: {[[B0]nos -> (D- => (phi -> K+ K-) (rho- -> pi- pi0)) K+]cc, [[B0]os -> (D+ => (phi -> K+ K-) (rho+ -> pi+ pi0)) K-]cc}
#
from Configurables import Generation
Generation().EventType = 11164455
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_DK,phirho=SVV,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
