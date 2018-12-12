# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/27462412.py generated: Wed, 25 Jan 2017 15:25:36
#
# Event Type: 27462412
#
# ASCII decay Descriptor: [D*(2007)0 -> (D0 -> {K- pi+}) (pi0,gamma)]cc
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/DStarZeroCut.py" )
from Configurables import Generation
Generation().EventType = 27462412
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Dst0_D0pi0_D0gamma,Kpi=DStarZeroCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/DStarZeroCut"
Generation().SignalPlain.SignalPIDList = [ 423,-423 ]
