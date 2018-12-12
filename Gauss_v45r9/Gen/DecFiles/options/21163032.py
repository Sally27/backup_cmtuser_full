# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/21163032.py generated: Fri, 27 Mar 2015 16:10:09
#
# Event Type: 21163032
#
# ASCII decay Descriptor: [D+ -> pi- pi+ K+]cc
#
from Configurables import Generation
Generation().EventType = 21163032
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D+_pi-pi+K+=phsp,TightCut2.dec"
Generation().SignalPlain.CutTool = "'LoKi::GenCutTool/TightCut'"
Generation().SignalPlain.SignalPIDList = [ 411,-411 ]

#
from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
gen = Generation()
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = '^[ D+ => ^pi- ^pi+ ^K+]CC'
tightCut.Preambulo += [
    "GVZ = LoKi.GenVertices.PositionZ() " ,
    "from GaudiKernel.SystemOfUnits import millimeter" ,
    "inAcc = in_range ( 0.010, GTHETA, 0.400 ) " , 
    "daughcuts = ( (GPT > 250 * MeV) & ( GP > 2000 * MeV))",
    "Dcuts = ( (GPT > 2100 * MeV) & ( GP > 14000 * MeV))"
]
tightCut.Cuts      =    {
    '[K+]cc'  : ' inAcc & daughcuts',
    '[pi+]cc'  : ' inAcc & daughcuts',
    '[D+]cc'   : 'Dcuts'
                        }
