# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/30000091.py generated: Fri, 27 Mar 2015 15:48:10
#
# Event Type: 30000091
#
# ASCII decay Descriptor: pp => ?
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Diffractive.py" )
from Configurables import Generation
Generation().EventType = 30000091
Generation().SampleGenerationTool = "MinimumBias"
from Configurables import MinimumBias
Generation().addTool( MinimumBias )
Generation().MinimumBias.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/minbias_diffractive.dec"
Generation().MinimumBias.CutTool = ""
