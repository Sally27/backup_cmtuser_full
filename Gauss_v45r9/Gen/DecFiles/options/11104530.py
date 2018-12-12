# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11104530.py generated: Fri, 27 Mar 2015 16:10:04
#
# Event Type: 11104530
#
# ASCII decay Descriptor: [B0 -> (anti-Lambda0 -> anti-p- pi+) (rho- -> pi- pi0) p+]cc
#
from Configurables import Generation
Generation().EventType = 11104530
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Lambdap-rho+,Lambdagamma=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
