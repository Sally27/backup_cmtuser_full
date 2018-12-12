# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/10010037.py generated: Wed, 25 Jan 2017 15:25:30
#
# Event Type: 10010037
#
# ASCII decay Descriptor: pp => [<Xb>]cc ...
#
from Configurables import Generation
Generation().EventType = 10010037
Generation().SampleGenerationTool = "Inclusive"
from Configurables import Inclusive
Generation().addTool( Inclusive )
Generation().Inclusive.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_b=CharmtoKplusmu,PPTcuts,InAcc.dec"
Generation().Inclusive.CutTool = "LHCbAcceptance"
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/b2Charm2KplusmuFilterPPTcuts"
Generation().Inclusive.InclusivePIDList = [ 521, -521, 511, -511, 531, -531, 541, -541, 5122, -5122, 5222, -5222, 5212, -5212, 5112, -5112, 5312, -5312, 5322, -5322, 5332, -5332, 5132, -5132, 5232, -5232 ]

from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "b2Charm2KplusmuFilterPPTcuts" )
SignalFilter = Generation().b2Charm2KplusmuFilterPPTcuts
SignalFilter.Code = " has(isB2Charm2KplusmuPPTcuts)"
SignalFilter.Preambulo += [
 "from GaudiKernel.SystemOfUnits import  GeV",
 "isB2Charm2KplusmuRaw = (GBEAUTY & (GDECTREE('[(Beauty & LongLived) -> (Charm --> K+ ...) mu-  ...]CC')))",
"isnotmuonfromKL  = ~(GBEAUTY & GDECTREE('[(Beauty & LongLived) --> ([KL0 -> mu+...]CC) ...]CC'))",
 "mucuts = (GINTREE ( (('mu-' == GABSID ) & (GP > 5 * GeV) &  (GPT > 1 * GeV)) ) )",
 "Kcuts = (GINTREE ( ( ('K+' == GABSID ) & (GP > 7 * GeV) & (GPT > 0.3 * GeV)) ) )",
"isB2Charm2KplusmuPPTcuts          = ( isB2Charm2KplusmuRaw  & isnotmuonfromKL & mucuts & Kcuts)"
   ]

