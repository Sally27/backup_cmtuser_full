# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/15102203.py generated: Wed, 25 Jan 2017 15:25:25
#
# Event Type: 15102203
#
# ASCII decay Descriptor: [Lambda_b0 -> (Lambda(1520)0 -> p+ K-) gamma]cc
#
from Configurables import Generation
Generation().EventType = 15102203
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_gammaLambda1520=HighPtGamma,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/BRadiativeCut"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]

from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "BRadiativeCut" )
radCut = Generation().BRadiativeCut
radCut.Code = " ( count ( isGoodB ) > 0 ) "
radCut.Preambulo += [
    "from GaudiKernel.SystemOfUnits import  GeV, mrad"
  , "NGoodGamma = GINTREE(('gamma' == GABSID) & (GPT >1.5*GeV))"
  , "isGoodB    = (GBEAUTY & NGoodGamma)"
   ]

