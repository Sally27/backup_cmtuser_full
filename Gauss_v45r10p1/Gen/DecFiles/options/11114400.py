# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11114400.py generated: Wed, 25 Jan 2017 15:25:25
#
# Event Type: 11114400
#
# ASCII decay Descriptor: {[[B0]nos -> mu+ mu- (omega(782) -> pi+ pi- (pi0 -> gamma gamma))]cc, [[B0]os -> mu- mu+ (omega(782) -> pi+ pi- (pi0 -> gamma gamma))]cc}
#
from Configurables import Generation
Generation().EventType = 11114400
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_omega2pipipi_mumu=MS,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
