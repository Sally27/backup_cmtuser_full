# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/25113001.py generated: Fri, 27 Mar 2015 16:10:18
#
# Event Type: 25113001
#
# ASCII decay Descriptor: [Lambda_c+ -> p- mu+ mu+]cc
#
from Configurables import Generation
Generation().EventType = 25113001
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lc_pmumu=SS,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 4122,-4122 ]
