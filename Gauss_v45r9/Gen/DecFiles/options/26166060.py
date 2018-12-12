# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/26166060.py generated: Fri, 27 Mar 2015 16:10:12
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
from Configurables import Gauss
Generation().Special.GenXiccProduction.BeamMomentum = Gauss().BeamMomentum
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
Generation().Special.GenXiccProduction.GenXiccCommands += GenXiccListOfCommands

from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [
### The mass of Xi_cc++ can not be set here. The value 3.7 is just for consistency.
###                  GEANTID       PDGID  CHARGE      MASS(GeV)        TLIFE(s)               EVTGENNAME    PYTHIAID        MAXWIDTH
    "Xi_cc++             506        4422     2.0            3.7       4.50e-013                  Xi_cc++        4422   0.000000e+000",
    "Xi_cc~--            507       -4422    -2.0            3.7       4.50e-013             anti-Xi_cc--       -4422   0.000000e+000"
]


