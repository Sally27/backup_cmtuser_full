# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11164461.py generated: Fri, 27 Mar 2015 16:10:00
#
# Event Type: 11164461
#
# ASCII decay Descriptor: {[[B0]nos -> (D*(2010)- -> (D~0 -> K+ pi-) pi- ) (K*(892)+ -> K+ pi0)]cc, [[B0]os -> (D*(2010)+ -> (D0 -> K- pi+) pi- ) (K*(892)- -> K- pi0)]cc}
#
from Configurables import Generation
Generation().EventType = 11164461
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dst-Kst+,D0pi-,Kpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
