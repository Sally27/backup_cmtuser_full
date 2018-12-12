# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11134060.py generated: Fri, 27 Mar 2015 16:10:09
#
# Event Type: 11134060
#
# ASCII decay Descriptor: [B0 -> (chi_c2(1P) -> pi+ pi-) (K*(892)0 -> K+ pi-) ]cc
#
from Configurables import Generation
Generation().EventType = 11134060
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_chic2Kst,pipi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
