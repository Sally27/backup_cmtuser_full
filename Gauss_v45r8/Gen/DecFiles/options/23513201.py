# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/23513201.py generated: Fri, 27 Mar 2015 15:48:01
#
# Event Type: 23513201
#
# ASCII decay Descriptor: [D_s+ => ( eta => gamma mu+ mu- ) mu+ nu_mu]cc
#
from Configurables import Generation
Generation().EventType = 23513201
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds_etamunu,gmm=Eta2MuMuGamma,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 431,-431 ]
