# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/21163022.py generated: Fri, 27 Mar 2015 15:47:57
#
# Event Type: 21163022
#
# ASCII decay Descriptor: [D+ -> K- pi+ pi+]cc
#
from Configurables import Generation
Generation().EventType = 21163022
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D+_K-pi+pi+=phsp,TightCut2.dec"
Generation().SignalPlain.CutTool = "'LoKi::GenCutTool/TightCut'"
Generation().SignalPlain.SignalPIDList = [ 411,-411 ]

#
from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
gen = Generation()
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = '^[ D+ => ^K- ^pi+ ^pi+]CC'
tightCut.Preambulo += [
    "GVZ = LoKi.GenVertices.PositionZ() " ,
    "from GaudiKernel.SystemOfUnits import millimeter" ,
    "inAcc = in_range ( 0.010, GTHETA, 0.400 ) " , 
    "daughcuts = ( (GPT > 250 * MeV) & ( GP > 2000 * MeV))",
    "Dcuts = ( (GPT > 2100 * MeV) & ( GP > 14000 * MeV))"
]
tightCut.Cuts      =    {
    '[K-]cc'  : ' inAcc & daughcuts',
    '[pi+]cc'  : ' inAcc & daughcuts',
    '[D+]cc'   : 'Dcuts'
                        }

