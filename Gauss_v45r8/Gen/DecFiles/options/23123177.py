# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/23123177.py generated: Fri, 27 Mar 2015 15:48:03
#
# Event Type: 23123177
#
# ASCII decay Descriptor: [D_s+ -> (KS0 -> pi+ pi-) e+ nu_e]cc
#
from Configurables import Generation
Generation().EventType = 23123177
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds+_Kse+nu_e=phsp,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 431,-431 ]
