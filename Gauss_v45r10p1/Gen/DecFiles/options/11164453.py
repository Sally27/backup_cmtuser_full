# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11164453.py generated: Wed, 25 Jan 2017 15:25:27
#
# Event Type: 11164453
#
# ASCII decay Descriptor: {[[B0]nos -> (D_s- => (phi -> K+ K-) (rho- -> pi- pi0)) K+]cc, [[B0]os -> (D_s+ => (phi -> K+ K-) (rho+ -> pi+ pi0)) K-]cc}
#
from Configurables import Generation
Generation().EventType = 11164453
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_DsK,phirho=SVV,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
