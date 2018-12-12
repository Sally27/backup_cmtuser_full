# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/15102213.py generated: Wed, 25 Jan 2017 15:25:22
#
# Event Type: 15102213
#
# ASCII decay Descriptor: [Lambda_b0 -> p+ K- gamma]cc
#
from Configurables import Generation
Generation().EventType = 15102213
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_gammapK=HighPtGamma,DecProdCut.dec"
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
  , "isGoodB    = (GBEAUTY & NGoodGamma & GDECTREE('[Lambda_b0 -> p+ K- gamma]CC'))"
   ]

