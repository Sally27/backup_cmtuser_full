# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/41900011.py generated: Wed, 25 Jan 2017 15:25:33
#
# Event Type: 41900011
#
# ASCII decay Descriptor: pp => (t => b ...) (t~ => b~ ...) ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Top_ttbar.py" )
from Configurables import Generation
Generation().EventType = 41900011
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/ttbar_bb,2binAcc.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/TwoBFromTop"

from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "TwoBFromTop" )
tracksInAcc = Generation().TwoBFromTop
tracksInAcc.Code = "  ( count ( isGoodBfromT ) > 1 ) "
tracksInAcc.Preambulo += [
     "from GaudiKernel.SystemOfUnits import  GeV, mrad"
   , "isGoodBfromT   = ( (  'b' == GABSID ) & GINTREE( GBEAUTY ) )"
   ]

