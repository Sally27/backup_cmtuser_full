# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11296020.py generated: Fri, 27 Mar 2015 16:10:18
#
# Event Type: 11296020
#
# ASCII decay Descriptor: {[[B0]nos -> (D_s+ => K- K+ pi+) (D*(2010)- -> pi- (D~0 -> K+ pi-))]cc, [[B0]os -> (D_s- => K+ K- pi-) (D*(2010)+ -> pi+ (D0 -> K- pi+))]cc}
#
from Configurables import Generation
Generation().EventType = 11296020
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_DsDst.dec"
Generation().SignalRepeatedHadronization.CutTool = "LHCbAcceptance"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
