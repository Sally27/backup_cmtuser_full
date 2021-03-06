# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/23265000.py generated: Fri, 27 Mar 2015 15:47:56
#
# Event Type: 23265000
#
# ASCII decay Descriptor: [D_s+ => K- K+ pi- pi+ pi+]cc
#
from Configurables import Generation
Generation().EventType = 23265000
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds+_K-K+pi-pi+pi+=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 431,-431 ]
