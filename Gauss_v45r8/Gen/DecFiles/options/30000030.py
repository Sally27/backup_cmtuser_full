# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/30000030.py generated: Fri, 27 Mar 2015 15:48:05
#
# Event Type: 30000030
#
# ASCII decay Descriptor: pp => ?
#
from Configurables import Generation
Generation().EventType = 30000030
Generation().SampleGenerationTool = "MinimumBias"
from Configurables import MinimumBias
Generation().addTool( MinimumBias )
Generation().MinimumBias.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/minbias=HardScattering,pt30GeV.dec"
Generation().MinimumBias.CutTool = ""

from Configurables import PythiaProduction
Generation().MinimumBias.addTool( PythiaProduction )
Generation().MinimumBias.PythiaProduction.Commands += ["pysubs ckin 3 30."]

