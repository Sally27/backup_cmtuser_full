# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11296402.py generated: Fri, 27 Mar 2015 15:48:00
#
# Event Type: 11296402
#
# ASCII decay Descriptor: {[B0 -> (D- -> K+ pi- pi-) (D+ -> pi- pi+ pi+ pi0)]cc,[B0 -> (D- -> K+ pi- pi-) (D_s+ -> pi- pi+ pi+ pi0)]cc,[B0 -> (D- -> K+ pi- pi-) (D_s*+ -> gamma (D_s+ -> pi- pi+ pi+ pi0))]cc,[B0 -> (D- -> K+ pi- pi-) (D*+ -> (D+ -> pi- pi+ pi+ pi0) pi0)]cc}
#
from Configurables import Generation
Generation().EventType = 11296402
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D-Xc,Xc2hhhpi0=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
