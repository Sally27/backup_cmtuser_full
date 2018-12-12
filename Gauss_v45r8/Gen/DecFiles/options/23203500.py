# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/23203500.py generated: Fri, 27 Mar 2015 15:48:07
#
# Event Type: 23203500
#
# ASCII decay Descriptor: [Ds+ ->  (KS0 -> pi+ pi-) pi+ pi0]cc
#
from Configurables import Generation
Generation().EventType = 23203500
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds_KSpipi0=res,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 431,-431 ]
