# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/26164026.py generated: Wed, 25 Jan 2017 15:25:27
#
# Event Type: 26164026
#
# ASCII decay Descriptor: [ Sigma_c++ -> ( Lambda_c+ -> p+ K- pi+) pi+ ]cc
#
from Configurables import Generation
Generation().EventType = 26164026
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Sigma_c++,Lc,pKpi=phsp,TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 4222,-4222 ]

#
from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
generation = Generation() 
#signal     = generation.SignalPlain 
signal     = generation.SignalRepeatedHadronization 
signal.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut   = signal.TightCut
tightCut.Decay     = '[ Sigma_c++ => ^( Lambda_c+ ==> ^p+ ^K- ^pi+) pi+ ]CC'
tightCut.Preambulo += [
    'from GaudiKernel.SystemOfUnits import millimeter, micrometer,MeV,GeV',
    'GY           =  LoKi.GenParticles.Rapidity () ## to be sure ' , 
    'inAcc        =  in_range ( 0.005 , GTHETA , 0.400 )         ' ,
    'inEta        =  in_range ( 1.95  , GETA   , 5.050 )         ' ,
    'fastTrack    =  ( GPT > 220 * MeV ) & ( GP  > 3.0 * GeV )   ' , 
    'goodTrack    =  inAcc & inEta & fastTrack                   ' ,     
    'longLived    =  75 * micrometer < GTIME                     ' , 
    'inY          =  in_range ( 1.9   , GY     , 4.6   )         ' , 
    'goodLc       =  inY & longLived     & ( GPT > 0.9 * GeV )   ' ,
    'Bancestors   =  GNINTREE ( GBEAUTY , HepMC.ancestors )      ' , 
    'notFromB     =  0 == Bancestors                             ' , 
]
tightCut.Cuts     =    {
    '[Lambda_c+]cc'  : 'goodLc & notFromB ' ,
    '[K+]cc'         : 'goodTrack ' , 
    '[pi+]cc'        : 'goodTrack ' , 
    '[p+]cc'         : 'goodTrack & ( GP > 9 * GeV ) '
    }

# Generator efficiency histos:
tightCut.XAxis = ( "GCHILD(GPT,'Lambda_c+'==GABSID)/GeV" , 1.0 , 20.0 , 38  )
tightCut.YAxis = ( "GCHILD(GY ,'Lambda_c+'==GABSID)   "  , 2.0 ,  4.5 , 10  )


