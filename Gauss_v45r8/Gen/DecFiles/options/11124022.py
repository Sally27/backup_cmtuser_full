# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11124022.py generated: Fri, 27 Mar 2015 15:48:07
#
# Event Type: 11124022
#
# ASCII decay Descriptor: {[[B0]nos -> e+ e- (rho0 -> pi+ pi-)]cc, [[B0]os -> e- e+ (rho -> pi- pi+)]cc}
#
from Configurables import Generation
Generation().EventType = 11124022
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_rhoee=MS,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
