# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11102222.py generated: Fri, 27 Mar 2015 15:48:11
#
# Event Type: 11102222
#
# ASCII decay Descriptor: [B0 -> (rho0 -> pi+ pi-) gamma]cc
#
from Configurables import Generation
Generation().EventType = 11102222
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_rhogamma,pipi=HighPtGamma,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/BRadiativeCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]

from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "BRadiativeCut" )
radCut = Generation().BRadiativeCut
radCut.Code = " ( count ( isGoodB ) > 0 ) "
radCut.Preambulo += [
    "from GaudiKernel.SystemOfUnits import  GeV, mrad"
  , "NGoodGamma = GINTREE(('gamma' == GABSID) & (GPT >1.5*GeV))"
  , "isGoodB    = (GBEAUTY & NGoodGamma)"
   ]

