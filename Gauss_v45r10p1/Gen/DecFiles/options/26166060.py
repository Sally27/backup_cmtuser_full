# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/26166060.py generated: Wed, 25 Jan 2017 15:25:34
#
# Event Type: 26166060
#
# ASCII decay Descriptor: [Xi_cc++ -> (D0 -> pi+ K-) p+ K- pi+ pi+]cc
#
from Configurables import Generation
Generation().EventType = 26166060
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "GenXiccProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import GenXiccProduction
Generation().Special.addTool( GenXiccProduction )
Generation().Special.GenXiccProduction.BaryonState = "Xi_cc++"
Generation().Special.GenXiccProduction.Commands = ["mixevnt imix 1", "loggrade ivegasopen 0", "loggrade igrade 1", "vegasbin nvbin 300", "counter xmaxwgt 5000000", "confine pscutmin 0.0", "confine pscutmax 7.0"]
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xicc++_D0pKpipi,Kpi=DecProdCut,WithMinPT.dec"
Generation().Special.CutTool = "XiccDaughtersInLHCbAndWithMinPT"
from Configurables import XiccDaughtersInLHCbAndWithMinPT
Generation().Special.addTool( XiccDaughtersInLHCbAndWithMinPT )
Generation().Special.XiccDaughtersInLHCbAndWithMinPT.BaryonState = Generation().Special.GenXiccProduction.BaryonState


GenXiccListOfCommands = [ 
  "subopen ichange 1"
 ,"upcom pmb 1.85"
 ,"upcom pmc 1.85"
]
Generation().Special.addTool( GenXiccProduction , name = "GenXiccProduction" )
Generation().Special.GenXiccProduction.Commands += GenXiccListOfCommands

from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [
### The mass of Xi_cc++ can not be set here. The value 3.7 is just for consistency.
###                  GEANTID       PDGID  CHARGE      MASS(GeV)        TLIFE(s)               EVTGENNAME    PYTHIAID        MAXWIDTH
    "Xi_cc++             506        4422     2.0            3.7       4.50e-013                  Xi_cc++        4422   0.000000e+000",
    "Xi_cc~--            507       -4422    -2.0            3.7       4.50e-013             anti-Xi_cc--       -4422   0.000000e+000"
]


