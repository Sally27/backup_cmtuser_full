# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11164401.py generated: Fri, 27 Mar 2015 15:48:14
#
# Event Type: 11164401
#
# ASCII decay Descriptor: {[[B0]nos -> (D- => K+ pi- pi-) (rho+ -> pi+ (pi0->gamma gamma))]cc, [[B0]os -> (D+ => K- pi+ pi+) (rho- ->pi- (pi0->gamma gamma)))]cc}
#
from Configurables import Generation
Generation().EventType = 11164401
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D-rho+=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
