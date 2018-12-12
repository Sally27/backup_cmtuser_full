# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/16145133.py generated: Fri, 27 Mar 2015 15:48:01
#
# Event Type: 16145133
#
# ASCII decay Descriptor: [Xi_b- -> (Xi- -> (Lambda0 -> p+ pi-) pi-) (J/psi(1S) -> mu+ mu-)]cc
#
from Configurables import Generation
Generation().EventType = 16145133
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xib_JpsiXi,mm,Lambdapi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5132,-5132 ]
