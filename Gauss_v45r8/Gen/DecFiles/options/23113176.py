# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/23113176.py generated: Fri, 27 Mar 2015 15:48:09
#
# Event Type: 23113176
#
# ASCII decay Descriptor: [Ds+ -> (KS0 -> pi+ pi-) mu+ nu_mu]cc
#
from Configurables import Generation
Generation().EventType = 23113176
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds+_Ksmu+nu_mu=phsp,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 431,-431 ]
