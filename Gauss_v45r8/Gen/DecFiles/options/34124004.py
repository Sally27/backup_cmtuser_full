# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/34124004.py generated: Fri, 27 Mar 2015 15:48:03
#
# Event Type: 34124004
#
# ASCII decay Descriptor: K_S0 -> pi+ pi- e+ e-
#
from Configurables import Generation
Generation().EventType = 34124004
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/KS_pipiee=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 310 ]
