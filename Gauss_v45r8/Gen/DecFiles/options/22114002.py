# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/22114002.py generated: Fri, 27 Mar 2015 15:48:15
#
# Event Type: 22114002
#
# ASCII decay Descriptor: [D0 -> pi+ pi- mu+ mu-]cc
#
from Configurables import Generation
Generation().EventType = 22114002
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D0_pipimumu=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 421,-421 ]
