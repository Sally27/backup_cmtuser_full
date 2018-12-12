# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/22264000.py generated: Fri, 27 Mar 2015 15:47:59
#
# Event Type: 22264000
#
# ASCII decay Descriptor: [D0 -> K- pi- pi+ pi+]cc
#
from Configurables import Generation
Generation().EventType = 22264000
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D0_Kpipipi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "LHCbAcceptance"
Generation().SignalPlain.SignalPIDList = [ 421,-421 ]
