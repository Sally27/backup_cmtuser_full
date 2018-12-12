# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/41900005.py generated: Fri, 27 Mar 2015 16:10:18
#
# Event Type: 41900005
#
# ASCII decay Descriptor: pp => (t => b ...) (t~ => b~ ...) ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Top.py" )
from Configurables import Generation
Generation().EventType = 41900005
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/tt_bb=1l,10GeV,2b.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/TwoBOneLeptonFromTop"

from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "TwoBOneLeptonFromTop" )
tracksInAcc = Generation().TwoBOneLeptonFromTop
tracksInAcc.Code = " ( (count ( isGoodbquark ) > 1) & (count ( isGoodLepton ) >0)) "
tracksInAcc.Preambulo += [
     "from GaudiKernel.SystemOfUnits import  GeV, mrad"
   , "isGoodbquark   = ((  't' == GABSID ) & GINTREE( GBEAUTY & ( GTHETA < 400.0*mrad )))"
   , "isGoodLepton   = ((  'W+' == GABSID ) & GINTREE( GLEPTON & ( GTHETA < 400.0*mrad ) & (GPT > 10*GeV)))"
   ]

