# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11164091.py generated: Fri, 27 Mar 2015 15:47:58
#
# Event Type: 11164091
#
# ASCII decay Descriptor: {[[B0]nos -> pi+ (D*(2010)- -> pi- (D~0 -> K+ pi-))]cc, [[B0]os -> pi- (D*(2010)+ -> pi+ (D0 -> K- pi+))]cc}
#
from Configurables import Generation
Generation().EventType = 11164091
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dst-pi+,D0pi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
