# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/42900002.py generated: Wed, 25 Jan 2017 15:25:16
#
# Event Type: 42900002
#
# ASCII decay Descriptor: pp -> (Z0 -> c c~) ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Zcc.py" )
from Configurables import Generation
Generation().EventType = 42900002
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Z_cc.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/Zwith2cinAcc"

from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "Zwith2cinAcc" )
tracksInAcc = Generation().Zwith2cinAcc
tracksInAcc.Code = "count ( isGoodCFromZ ) > 1"
tracksInAcc.Preambulo += [
     "from GaudiKernel.SystemOfUnits import  GeV, mrad"
   , "isGoodC = ( ( 'c' == GABSID ) & ( GTHETA < 400.0*mrad ) )"
   , "isFromZ  = ( 1 == GNINTREE( 'Z0' == GABSID , 0 ) )"
   , "isGoodCFromZ = ( isGoodC & isFromZ )" ]

