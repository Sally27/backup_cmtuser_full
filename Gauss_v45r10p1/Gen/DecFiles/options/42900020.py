# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/42900020.py generated: Wed, 25 Jan 2017 15:25:29
#
# Event Type: 42900020
#
# ASCII decay Descriptor: pp -> [(W+ -> q q'bar)  ...]cc
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/W_inc.py" )
from Configurables import Generation
Generation().EventType = 42900020
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/W_qq.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/HadronInAcc"

from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "HadronInAcc" )
tracksInAcc = Generation().HadronInAcc
tracksInAcc.Code = "count ( isGoodHadronFromW ) > 1"
tracksInAcc.Preambulo += [
     "from GaudiKernel.SystemOfUnits import  GeV, mrad"
   , "isGoodHadron = ( (( 'u' == GABSID ) | ( 'd' == GABSID ) | ( 's' == GABSID ) | ( 'c' == GABSID ))& ( GTHETA < 400.0*mrad ) )"
   , "isFromW  = ( 1 == GNINTREE( 'W+' == GABSID , 0 ) )"
   , "isGoodHadronFromW = ( isGoodHadron & isFromW )" ]

