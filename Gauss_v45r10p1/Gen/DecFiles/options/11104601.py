# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11104601.py generated: Wed, 25 Jan 2017 15:25:18
#
# Event Type: 11104601
#
# ASCII decay Descriptor: [B0 -> (eta' -> pi+ pi- gamma ) (omega(782) -> pi+ pi- (pi0 -> gamma gamma) )]cc
#
from Configurables import Generation
Generation().EventType = 11104601
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_omegaetap,pipig=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
