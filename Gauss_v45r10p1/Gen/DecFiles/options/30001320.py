# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/30001320.py generated: Wed, 25 Jan 2017 15:25:20
#
# Event Type: 30001320
#
# ASCII decay Descriptor: pp => ?
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Perugia0_DefaultPythiaProcesses.py" )
from Configurables import Generation
Generation().EventType = 30001320
Generation().SampleGenerationTool = "MinimumBias"
from Configurables import MinimumBias
Generation().addTool( MinimumBias )
Generation().MinimumBias.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/minbias_Perugia0WithDefaultPythiaProcesses.dec"
Generation().MinimumBias.CutTool = ""
