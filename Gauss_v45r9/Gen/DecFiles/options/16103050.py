# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/16103050.py generated: Fri, 27 Mar 2015 16:10:18
#
# Event Type: 16103050
#
# ASCII decay Descriptor: [Omega_b-  -> K- K- p+]cc
#
from Configurables import Generation
Generation().EventType = 16103050
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Omegab_KKp=sqDalitz,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5332,-5332 ]
