# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/34102107.py generated: Wed, 25 Jan 2017 15:25:21
#
# Event Type: 34102107
#
# ASCII decay Descriptor: K_S0 -> pi+ pi-
#
from Configurables import Generation
Generation().EventType = 34102107
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ks_pipi=TightCut,rho.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 310 ]

#
from Configurables import LoKi__GenCutTool
gen = Generation()
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' )
#
tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = 'KS0 -> pi+ pi-'
tightCut.Preambulo += [
    "from GaudiKernel.SystemOfUnits import meter, millimeter, GeV" ,
    "GVX = LoKi.GenVertices.PositionX() " ,
    "GVY = LoKi.GenVertices.PositionY() " ,
    "GVZ = LoKi.GenVertices.PositionZ() " ,
    "vx    = GFAEVX ( GVX, 100 * meter ) " ,    
    "vy    = GFAEVX ( GVY, 100 * meter ) " ,
    "vz    = GFAEVX ( GVZ, 100 * meter ) " ,
    "rho2  = vx**2 + vy**2 " ,
    "rhoK  = rho2 < (38 * millimeter )**2 " , 
    "decay = vz   < (0.8 * meter ) ",
]
tightCut.Cuts      =    {
    'KS0'  : ' decay & rhoK',
                        }

