# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/30000042.py generated: Fri, 27 Mar 2015 16:10:09
#
# Event Type: 30000042
#
# ASCII decay Descriptor: pp => [bbbar] ...
#
from Configurables import Generation
Generation().EventType = 30000042
Generation().SampleGenerationTool = "MinimumBias"
from Configurables import MinimumBias
Generation().addTool( MinimumBias )
Generation().MinimumBias.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/minbias=HardScattering,pt20,pt40GeV,incl_b.dec"
Generation().MinimumBias.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/twobinAcc"

from Configurables import PythiaProduction
Generation().MinimumBias.addTool( PythiaProduction )
Generation().MinimumBias.PythiaProduction.Commands += ["pysubs ckin 3 20."]
Generation().MinimumBias.PythiaProduction.Commands += ["pysubs ckin 4 40."]
from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "twobinAcc" )
tracksInAcc = Generation().twobinAcc
tracksInAcc.Code = "count ( isGoodB ) > 1"
tracksInAcc.Preambulo += [
     "from GaudiKernel.SystemOfUnits import  GeV, mrad"
   , "isGoodB = ( ( 'b' == GABSID ) & ( GTHETA < 400.0*mrad ) & ( GPT > 5.0*GeV ) )" ]

