# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/21123177.py generated: Fri, 27 Mar 2015 15:48:08
#
# Event Type: 21123177
#
# ASCII decay Descriptor: [D+ -> (KS0 -> pi+ pi-) e+ nu_e]cc
#
from Configurables import Generation
Generation().EventType = 21123177
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D+_Kse+nu_e=phsp,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 411,-411 ]
