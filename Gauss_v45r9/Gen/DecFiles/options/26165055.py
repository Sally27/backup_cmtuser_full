# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/26165055.py generated: Fri, 27 Mar 2015 16:10:10
#
# Event Type: 26165055
#
# ASCII decay Descriptor: [ Xi_cc+ -> (Lambda_c+ -> p K- pi+) K- pi+ ]cc
#
from Configurables import Generation
Generation().EventType = 26165055
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
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xicc_LambdacKpi,pKpi=DecProdCutv2.dec"
Generation().Special.CutTool = "XiccDaughtersInLHCb"
from Configurables import XiccDaughtersInLHCb
Generation().Special.addTool( XiccDaughtersInLHCb )
Generation().Special.XiccDaughtersInLHCb.BaryonState = Generation().Special.GenXiccProduction.BaryonState
