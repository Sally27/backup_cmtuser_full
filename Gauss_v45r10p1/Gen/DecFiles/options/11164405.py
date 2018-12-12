# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11164405.py generated: Wed, 25 Jan 2017 15:25:23
#
# Event Type: 11164405
#
# ASCII decay Descriptor: {[[B0]nos -> K+ (D*(2010)- -> pi0 (D- -> K+ pi- pi-))]cc, [[B0]os -> K- (D*(2010)+ -> pi+ (D+ -> K- pi+ pi+))]cc}
#
from Configurables import Generation
Generation().EventType = 11164405
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dst-K+,D-pi0=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
