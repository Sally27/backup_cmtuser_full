# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/20000030.py generated: Wed, 25 Jan 2017 15:25:31
#
# Event Type: 20000030
#
# ASCII decay Descriptor: pp => [ccbar] exclusive ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/ccbarjets_pthat_gt_20.py" )
from Configurables import Generation
Generation().EventType = 20000030
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_c=HardQCDScatter,TightCut.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/twocinAcc"

from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "twocinAcc" )
tracksInAcc = Generation().twocinAcc
tracksInAcc.Code = "count ( isGoodC ) > 1"
tracksInAcc.Preambulo += [
     "from GaudiKernel.SystemOfUnits import  GeV, mrad"
   , "isGoodC = ( ( 'c' == GABSID ) & ( GTHETA < 400.0*mrad ) )" ]

