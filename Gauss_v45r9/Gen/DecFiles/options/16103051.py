# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/16103051.py generated: Fri, 27 Mar 2015 16:10:07
#
# Event Type: 16103051
#
# ASCII decay Descriptor: [Omega_b-  -> K- pi- p+]cc
#
from Configurables import Generation
Generation().EventType = 16103051
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Omegab_Kpip=sqDalitz,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5332,-5332 ]
