# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/42112013.py generated: Fri, 27 Mar 2015 15:48:13
#
# Event Type: 42112013
#
# ASCII decay Descriptor: pp -> (Z0/gamma* -> mu+ mu-) ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/DrellYanmumu60GeV.py" )
from Configurables import Generation
Generation().EventType = 42112013
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/DrellYan_mumu=60GeV.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/TwoMuonsFromDYInAcc"

from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "TwoMuonsFromDYInAcc" )
muonsInAcc = Generation().TwoMuonsFromDYInAcc
muonsInAcc.Code = " count ( isDYWithMuonInAcc ) > 0 "
muonsInAcc.Preambulo += [
      "from GaudiKernel.SystemOfUnits import GeV, mrad"
    , "isMuonInAcc   = ( ( GABSID == 13 )  & ( GPT > 1.0*GeV ) & ( GTHETA < 400.0*mrad ) & ( ( GSTATUS == 1 ) | ( GSTATUS == 999 ) ))"
    , "isDYWithMuonInAcc = ( ( GNINTREE(  isMuonInAcc , 4 ) > 1 ) )"
    ]

