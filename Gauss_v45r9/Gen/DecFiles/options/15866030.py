# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/15866030.py generated: Fri, 27 Mar 2015 16:10:05
#
# Event Type: 15866030
#
# ASCII decay Descriptor: [ Lambda_b0 ->  (Lambda_c+ -> p+ K- pi+)  (tau- -> pi- pi+ pi- nu_tau) anti-nu_tau   ]cc
#
from Configurables import Generation
Generation().EventType = 15866030
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Lctaunu,pKpi=cocktail,tau3pi,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
