# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/23263021.py generated: Fri, 27 Mar 2015 15:48:10
#
# Event Type: 23263021
#
# ASCII decay Descriptor: [D_s+ -> K- K+ pi+]cc
#
from Configurables import Generation
Generation().EventType = 23263021
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds+_K-K+pi+=res,TightCut.dec"
Generation().SignalPlain.CutTool = "'LoKi::GenCutTool/TightCut'"
Generation().SignalPlain.SignalPIDList = [ 431,-431 ]

#
from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
gen = Generation()
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = '^[ D_s+ => ^K- ^K+ ^pi+]CC'
tightCut.Preambulo += [
    "GVZ = LoKi.GenVertices.PositionZ() " ,
    "from GaudiKernel.SystemOfUnits import millimeter" ,
    "inAcc = in_range ( 0.010, GTHETA, 0.400 ) " , 
    "daughcuts = ( (GPT > 220 * MeV) & ( GP > 2400 * MeV))",
    "Dcuts = ( (GPT > 2300 * MeV) & ( GP > 20000 * MeV))"
]
tightCut.Cuts      =    {
    '[K-]cc'  : ' inAcc & daughcuts',
    '[pi+]cc'  : ' inAcc & daughcuts',
    '[D_s+]cc'   : 'Dcuts'
                        }

