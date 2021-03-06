# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11104191.py generated: Fri, 27 Mar 2015 16:10:07
#
# Event Type: 11104191
#
# ASCII decay Descriptor: {[[B0]nos -> (rho -> pi+ pi-) (KS0 -> pi+ pi-) gamma]cc, [[B0]os -> (rho -> pi+ pi-) (KS0 -> pi+ pi-) gamma]cc}
#
from Configurables import Generation
Generation().EventType = 11104191
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_rhoKSgamma=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
