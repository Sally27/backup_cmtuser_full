# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/25103090.py generated: Wed, 25 Jan 2017 15:25:20
#
# Event Type: 25103090
#
# ASCII decay Descriptor: [Lambda_c+ -> p+ pi- pi+]cc
#
from Configurables import Generation
Generation().EventType = 25103090
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lc_ppipi=phsp,TightCut,NotFromB.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 4122,-4122 ]

#
from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
generation = Generation() 
signal     = generation.SignalPlain 
signal.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut   = signal.TightCut
tightCut.Decay     = '^[Lambda_c+ ==> ^p+ ^pi- ^pi+]CC'
tightCut.Preambulo += [
    "from GaudiKernel.SystemOfUnits import millimeter, micrometer,MeV,GeV",
    "GY           =  LoKi.GenParticles.Rapidity () ## to be sure " , 
    "inAcc        =  in_range ( 0.005 , GTHETA , 0.400 )         " ,
    "inEta        =  in_range ( 1.75  , GETA   , 5.15 )          " ,
    "goodTrack  =  inAcc & inEta & ( GPT > 190 * MeV )         " , 
    "goodPion     =  goodTrack & (GP > .9 * GeV )              " ,     
    "goodProton   =  goodTrack & (GP > 9.5 * GeV )             " ,     
    "inY          =  in_range ( 1.85   , GY     , 4.85   )       " ,
    "dauPT        =  GCHILD(GPT,('p+' == GABSID )) + GCHILD(GPT,('pi-' == GABSID )) + GCHILD(GPT,('pi+' == GABSID ))", 
    "goodLc       =  inY & ( GPT > 2.4 * GeV ) & ( GP > 15 * GeV )" ,
    "Bancestors   =  GNINTREE ( GBEAUTY , HepMC.ancestors )       " , 
    "notFromB     =  0 == Bancestors                              " , 

]
tightCut.Cuts     =    {
    "[Lambda_c+]cc"  : "goodLc & notFromB" ,
    "[p+]cc"         : "goodTrack & ( GP > 9.5 * GeV )"
    }

