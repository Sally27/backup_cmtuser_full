# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/36105100.py generated: Fri, 27 Mar 2015 15:48:15
#
# Event Type: 36105100
#
# ASCII decay Descriptor: [Omega- -> (Xi- ->(Lambda0->p+ pi-)pi-) pi+ pi-]cc
#
from Configurables import Generation
Generation().EventType = 36105100
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Omega_XiPiPi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "LHCbAcceptance"
Generation().SignalPlain.SignalPIDList = [ 3334,-3334 ]
