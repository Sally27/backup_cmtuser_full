# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/25113004.py generated: Fri, 27 Mar 2015 15:48:02
#
# Event Type: 25113004
#
# ASCII decay Descriptor: [Lambda_c+ -> mu+ (rho -> mumu) ]cc
#
from Configurables import Generation
Generation().EventType = 25113004
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lc_rhop,mumu=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 4122,-4122 ]
