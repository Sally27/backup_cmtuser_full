# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/42100200.py generated: Wed, 25 Jan 2017 15:25:31
#
# Event Type: 42100200
#
# ASCII decay Descriptor: pp -> (Z0gamma -> b b~ gamma {,gamma} {,gamma}) ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Zgammabb=PHOTOS.py" )
from Configurables import Generation
Generation().EventType = 42100200
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Zgamma_bb=PHOTOS.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/ParsInAcc"
                                                                           
from Configurables import LoKi__FullGenEventCut                                             
Generation().addTool( LoKi__FullGenEventCut, "ParsInAcc" )                               
ParsInAcc = Generation().ParsInAcc
ParsInAcc.Code = " ( count ( isGoodZ ) > 0 ) "
                                                                         
ParsInAcc.Preambulo += [                                                                  
     "from GaudiKernel.SystemOfUnits import  GeV, mrad"                                     
   , "isGoodZ     = ((  'Z0' == GABSID ) & (GNINTREE( GBEAUTY & ( GTHETA < 400.0*mrad )) > 1))" 
   ]                                                                                        

