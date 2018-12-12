# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11164701.py generated: Wed, 25 Jan 2017 15:25:27
#
# Event Type: 11164701
#
# ASCII decay Descriptor: [B0 -> (D0 -> (K_S0 -> pi+ pi-) pi0) (eta' -> pi+ pi- gamma)]cc
#
from Configurables import Generation
Generation().EventType = 11164701
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_etapD0,pi+pi-g,Kspi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
