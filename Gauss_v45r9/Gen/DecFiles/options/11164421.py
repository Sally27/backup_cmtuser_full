# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11164421.py generated: Fri, 27 Mar 2015 16:10:14
#
# Event Type: 11164421
#
# ASCII decay Descriptor: {[[B0]nos -> (D- => K+ K- pi-) (rho+ -> pi+ (pi0->gamma gamma))]cc, [[B0]os -> (D+ => K- K+ pi+) (rho- ->pi- (pi0->gamma gamma)))]cc}
#
from Configurables import Generation
Generation().EventType = 11164421
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D-rho+,KKpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
