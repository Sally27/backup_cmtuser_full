# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/30000000.py generated: Fri, 27 Mar 2015 16:10:01
#
# Event Type: 30000000
#
# ASCII decay Descriptor: pp => ?
#
from Configurables import Generation
Generation().EventType = 30000000
Generation().SampleGenerationTool = "MinimumBias"
from Configurables import MinimumBias
Generation().addTool( MinimumBias )
Generation().MinimumBias.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/minbias.dec"
Generation().MinimumBias.CutTool = ""
