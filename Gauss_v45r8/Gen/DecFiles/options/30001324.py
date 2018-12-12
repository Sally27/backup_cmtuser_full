# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/30001324.py generated: Fri, 27 Mar 2015 15:48:00
#
# Event Type: 30001324
#
# ASCII decay Descriptor: pp => ?
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/PerugiaNOCR_DefaultPythiaProcesses.py" )
from Configurables import Generation
Generation().EventType = 30001324
Generation().SampleGenerationTool = "MinimumBias"
from Configurables import MinimumBias
Generation().addTool( MinimumBias )
Generation().MinimumBias.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/minbias_PerugiaNOCRWithDefaultPythiaProcesses.dec"
Generation().MinimumBias.CutTool = ""
