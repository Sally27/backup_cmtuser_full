# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/34512105.py generated: Wed, 25 Jan 2017 15:25:19
#
# Event Type: 34512105
#
# ASCII decay Descriptor: K_S0 -> pi+ mu- nu_mu~
#
from Configurables import Generation
Generation().EventType = 34512105
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ks_pimunu=TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 310 ]

#
from Configurables import LoKi__GenCutTool
gen = Generation()
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' )
#
tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = 'KS0 -> pi+ mu- nu_mu~'
tightCut.Preambulo += [
    "GVZ = LoKi.GenVertices.PositionZ() " ,
    "from GaudiKernel.SystemOfUnits import meter, GeV" ,
    "decay = in_range ( -1 * meter,            GFAEVX ( GVZ, 100 * meter ),                    1 * meter ) ",
]
tightCut.Cuts      =    {
    'KS0'  : ' decay ',
                        }

