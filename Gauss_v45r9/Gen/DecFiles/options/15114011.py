# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/15114011.py generated: Fri, 27 Mar 2015 16:10:04
#
# Event Type: 15114011
#
# ASCII decay Descriptor: [Lambda_b0 -> p+ K- mu+ mu-]cc
#
from Configurables import Generation
Generation().EventType = 15114011
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_pKmumu=phsp,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
