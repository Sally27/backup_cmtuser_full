# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11164406.py generated: Fri, 27 Mar 2015 16:10:09
#
# Event Type: 11164406
#
# ASCII decay Descriptor: {[[B0]nos -> (D- -> K+ pi- pi-) (rho(770)+ -> pi+ pi0)]cc, [[B0]os -> (D+ -> K- pi+ pi+) (rho(770)- ->pi- pi0)]cc}
#
from Configurables import Generation
Generation().EventType = 11164406
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D-rho+,Kpipi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
