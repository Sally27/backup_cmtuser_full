# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/42112050.py generated: Fri, 27 Mar 2015 15:48:10
#
# Event Type: 42112050
#
# ASCII decay Descriptor: pp -> {(Z0 -> {mu+ mu-)) b}cc
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Zmumuqjet.py" )
from Configurables import Generation
Generation().EventType = 42112050
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Zbjet=mumu,InAcc.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/ZbjetCut"

from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "ZbjetCut" )
zbcut = Generation().ZbjetCut
zbcut.Code = " ( (count ( isGoodb ) > 0) & (count(isGoodZ) > 0))  "
zbcut.Preambulo += [
     "from GaudiKernel.SystemOfUnits import  GeV, mrad"
   , "isGoodb     = ((GBEAUTY)   & (GINTREE((GBEAUTY) & ( GTHETA < 420.0*mrad ))) &  (GINTREE(('Z0' == GABSID)) ))"
   , "isGoodZ     = ((  'Z0' == GABSID ) & (GNINTREE(('mu+' == GABSID) & ( GTHETA < 420.0*mrad ) )>1))"
   ]

