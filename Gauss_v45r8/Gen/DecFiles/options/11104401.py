# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11104401.py generated: Fri, 27 Mar 2015 15:48:03
#
# Event Type: 11104401
#
# ASCII decay Descriptor: [B0 -> (eta -> pi+ pi- pi0) (K*0 -> K+ pi- )]cc
#
from Configurables import Generation
Generation().EventType = 11104401
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Ksteta,pi+pi-pi0=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
