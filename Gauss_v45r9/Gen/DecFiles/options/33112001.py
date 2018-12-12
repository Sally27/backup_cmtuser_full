# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/33112001.py generated: Fri, 27 Mar 2015 16:10:00
#
# Event Type: 33112001
#
# ASCII decay Descriptor: [Lambda0 -> K+ mu-]cc
#
from Configurables import Generation
Generation().EventType = 33112001
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lambda_Kmu=PHSP,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 3122,-3122 ]
