# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/34102104.py generated: Fri, 27 Mar 2015 16:10:05
#
# Event Type: 34102104
#
# ASCII decay Descriptor: K_S0 -> pi+ pi-
#
from Configurables import Generation
Generation().EventType = 34102104
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ks_pipi=TightCut.dec"
Generation().SignalPlain.CutTool = "'LoKi::GenCutTool/TightCut'"
Generation().SignalPlain.SignalPIDList = [ 310 ]

#
from Configurables import LoKi__GenCutTool
gen = Generation()
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' )
#
tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = 'KS0 -> pi+ pi-'
tightCut.Preambulo += [
    "GVZ = LoKi.GenVertices.PositionZ() " ,
    "from GaudiKernel.SystemOfUnits import meter, GeV" ,
    "decay = in_range ( -1 * meter,            GFAEVX ( GVZ, 100 * meter ),                    1 * meter ) ",
]
tightCut.Cuts      =    {
    'KS0'  : ' decay ',
                        }

