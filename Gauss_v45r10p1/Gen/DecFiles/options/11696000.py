# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11696000.py generated: Wed, 25 Jan 2017 15:25:34
#
# Event Type: 11696000
#
# ASCII decay Descriptor: [B0-> (D- -> K+ pi- pi-)(D_s+ -> nu_tau (tau+ -> pi+ pi+ pi- anti-nu_tau))]cc
#
from Configurables import Generation
Generation().EventType = 11696000
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_DDs_TauNu=DDalitz,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
