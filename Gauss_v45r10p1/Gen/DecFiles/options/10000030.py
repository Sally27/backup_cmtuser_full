# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/10000030.py generated: Wed, 25 Jan 2017 15:25:22
#
# Event Type: 10000030
#
# ASCII decay Descriptor: pp => [bbbar] ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/qcdjets_pthat_gt_20.py" )
from Configurables import Generation
Generation().EventType = 10000030
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_b=HardQCDScatter,TightCut.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/twobinAcc"

from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "twobinAcc" )
tracksInAcc = Generation().twobinAcc
tracksInAcc.Code = "count ( isGoodB ) > 1"
tracksInAcc.Preambulo += [
     "from GaudiKernel.SystemOfUnits import  GeV, mrad"
   , "isGoodB = ( ( 'b' == GABSID ) & ( GTHETA < 400.0*mrad ) )" ]

