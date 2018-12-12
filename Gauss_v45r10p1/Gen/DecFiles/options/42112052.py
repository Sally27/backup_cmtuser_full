# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/42112052.py generated: Wed, 25 Jan 2017 15:25:33
#
# Event Type: 42112052
#
# ASCII decay Descriptor: pp -> {(Z0 -> {mu+ mu-)) c}cc
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Zmumuqjet.py" )
from Configurables import Generation
Generation().EventType = 42112052
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Zcjet=mu17,InAcc.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/ZcjetCut"

from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "ZcjetCut" )
zccut = Generation().ZcjetCut
zccut.Code = " ( (count ( isGoodc ) > 0) &(count(isGoodZ) > 0))  "
zccut.Preambulo += [
     "from GaudiKernel.SystemOfUnits import  GeV, mrad"
   , "isGoodc     = ((GCHARM) & (GINTREE((GCHARM) & (GTHETA < 420.0*mrad ))) &  (GINTREE(('Z0' == GABSID))) )"
   , "isGoodZ     = (('Z0' == GABSID ) & (GNINTREE(('mu+' == GABSID) & ( GTHETA < 420.0*mrad ) & ( GPT > 17*GeV) )>0))"
   ]

