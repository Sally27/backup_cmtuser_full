# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/26165052.py generated: Fri, 27 Mar 2015 15:48:03
#
# Event Type: 26165052
#
# ASCII decay Descriptor: [ Xi_cc+ -> (Lambda_c+ -> p K- pi+) K- pi+ ]cc
#
from Configurables import Generation
Generation().EventType = 26165052
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
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xicc_LcKpi,pKpi=DecProdCut,WithMinPTv2.dec"
Generation().Special.CutTool = "XiccDaughtersInLHCbAndWithMinPT"
from Configurables import XiccDaughtersInLHCbAndWithMinPT
Generation().Special.addTool( XiccDaughtersInLHCbAndWithMinPT )
Generation().Special.XiccDaughtersInLHCbAndWithMinPT.BaryonState = Generation().Special.GenXiccProduction.BaryonState
