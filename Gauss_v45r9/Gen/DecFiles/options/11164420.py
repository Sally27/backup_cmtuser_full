# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11164420.py generated: Fri, 27 Mar 2015 16:10:08
#
# Event Type: 11164420
#
# ASCII decay Descriptor: {[[B0]nos -> (D- => K+ K- pi-) (rho+ -> pi+ (pi0->gamma gamma))]cc, [[B0]os -> (D+ => K- K+ pi+) (rho- ->pi- (pi0->gamma gamma)))]cc}
#
from Configurables import Generation
Generation().EventType = 11164420
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D-rho+,KKpi.dec"
Generation().SignalRepeatedHadronization.CutTool = ""
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
