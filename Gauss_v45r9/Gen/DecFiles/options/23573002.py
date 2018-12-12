# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/23573002.py generated: Fri, 27 Mar 2015 16:10:05
#
# Event Type: 23573002
#
# ASCII decay Descriptor: [Ds+ ->  phi( K+ K-) mu+ nu_mu]cc
#
from Configurables import Generation
Generation().EventType = 23573002
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds+_phimunu.dec"
Generation().SignalPlain.CutTool = "LHCbAcceptance"
Generation().SignalPlain.SignalPIDList = [ 431,-431 ]
