# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/22112011.py generated: Wed, 25 Jan 2017 15:25:21
#
# Event Type: 22112011
#
# ASCII decay Descriptor: [D0 -> p+ mu-]cc
#
from Configurables import Generation
Generation().EventType = 22112011
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D0_pmu=PHSP,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 421,-421 ]
