# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11102404.py generated: Fri, 27 Mar 2015 15:48:02
#
# Event Type: 11102404
#
# ASCII decay Descriptor: {[[B0]nos -> pi+ pi- (pi0 -> gamma gamma)]cc, [[B0]os -> pi- pi+ (pi0 -> gamma gamma)]cc}
#
from Configurables import Generation
Generation().EventType = 11102404
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_pi+pi-pi0=DecProdCut,sqDalitz.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
