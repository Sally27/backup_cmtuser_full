# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/23103002.py generated: Fri, 27 Mar 2015 15:48:06
#
# Event Type: 23103002
#
# ASCII decay Descriptor: [D_s+ -> (phi(1020) -> K+ K-) pi+]cc
#
from Configurables import Generation
Generation().EventType = 23103002
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds_phipi,KK=TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 431,-431 ]

#
from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
generation = Generation() 
signal     = generation.SignalPlain 
signal.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut   = signal.TightCut
tightCut.Decay     = '^[D_s+ ==> ^K- ^K+ ^pi+]CC'
tightCut.Preambulo += [
    'from GaudiKernel.SystemOfUnits import millimeter, micrometer,MeV,GeV',
    'GY           =  LoKi.GenParticles.Rapidity () ## to be sure       ' , 
    'inAcc        =  in_range ( 0.005 , GTHETA , 0.400 )               ' ,
    'inEta        =  in_range ( 1.95  , GETA   , 5.050 )               ' ,
    'fastTrack    =  ( GPT > 220 * MeV ) & ( GP  > 3.0 * GeV )         ' , 
    'goodTrack    =  inAcc & inEta & fastTrack                         ' ,     
    'longLived    =  75 * micrometer < GTIME                           ' , 
    'inY          =  in_range ( 1.9   , GY     , 4.6   )               ' , 
    'goodDs       =  inY & longLived     & ( GPT > 0.9 * GeV )         ' ,
    'Bancestors   =  GNINTREE ( GBEAUTY , HepMC.ancestors )            ' , 
    'notFromB     =  0 == Bancestors                                   ' 
]
tightCut.Cuts     =    {
    '[D_s+]cc': 'goodDs & notFromB ' ,
    '[K+]cc'  : 'goodTrack ' , 
    '[pi+]cc' : 'goodTrack '
    }

