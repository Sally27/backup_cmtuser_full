# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/26165051.py generated: Fri, 27 Mar 2015 16:10:00
#
# Event Type: 26165051
#
# ASCII decay Descriptor: [Xi_cc+ -> (D+ => pi+ pi+ K-) p+ K- ]cc
#
from Configurables import Generation
Generation().EventType = 26165051
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "GenXiccProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import GenXiccProduction
Generation().Special.addTool( GenXiccProduction )
Generation().Special.GenXiccProduction.BaryonState = "Xi_cc+"
from Configurables import Gauss
Generation().Special.GenXiccProduction.BeamMomentum = Gauss().BeamMomentum
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xicc_D+pK,Kpipi=DecProdCut,WithMinPTv2.dec"
Generation().Special.CutTool = "XiccDaughtersInLHCbAndWithMinPT"
from Configurables import XiccDaughtersInLHCbAndWithMinPT
Generation().Special.addTool( XiccDaughtersInLHCbAndWithMinPT )
Generation().Special.XiccDaughtersInLHCbAndWithMinPT.BaryonState = Generation().Special.GenXiccProduction.BaryonState
