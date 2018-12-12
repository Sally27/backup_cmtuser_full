# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11164430.py generated: Fri, 27 Mar 2015 15:48:02
#
# Event Type: 11164430
#
# ASCII decay Descriptor: {[[B0]nos -> (D*(2010)- -> (D~0 -> K+ pi-) pi- ) (rho(770)+ -> pi+ pi0)]cc, [[B0]os -> (D*(2010)+ -> (D0 -> K- pi+) pi- ) (rho(770)- -> pi- pi0)]cc}
#
from Configurables import Generation
Generation().EventType = 11164430
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dst-rho+,D0pi-=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
