# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/42163200.py generated: Wed, 25 Jan 2017 15:25:18
#
# Event Type: 42163200
#
# ASCII decay Descriptor: pp -> [W+ -> (D_s+ -> K+ K- pi+) gamma]cc ...
#
from Configurables import Generation
Generation().EventType = 42163200
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/W_Dsgamma=NoCut.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/ParsInAcc"

from Configurables import LoKi__FullGenEventCut 
Generation().addTool( LoKi__FullGenEventCut, "ParsInAcc" ) 
ParsInAcc = Generation().ParsInAcc

ParsInAcc.Code = " ( count ( isGoodW ) > 0 ) "

ParsInAcc.Preambulo += [
    "from GaudiKernel.SystemOfUnits import millimeter, micrometer,MeV,GeV"
    ,"GY           =  LoKi.GenParticles.Rapidity ()               "
    ,"isGoodW     = ((  'W+' == GABSID ) & (GY > 0))" 
    ]

Generation().DecayTool = ""
Generation().Special.DecayTool = ""

from Configurables import Generation
from Gaudi.Configuration import *

Generation().PileUpTool = "FixedLuminosityForRareProcess"

importOptions( "$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py" )

from Configurables import Special, Pythia8Production

Generation().addTool( Special )
Generation().Special.addTool( Pythia8Production )

Generation().Special.Pythia8Production.Commands += [
"SpaceShower:rapidityOrder = off", 
"WeakSingleBoson:ffbar2W = on",
"24:addChannel = 1 1. 101 431 22", 
"24:onMode = off", 
"24:onIfAny = 431", 
"431:addChannel = 1 1. 101 321 -321 211",
"431:onMode = off",##"431:onIfMatch = 321 -321 211",
"431:onIfMatch = 321 -321 211",
                                       ]


