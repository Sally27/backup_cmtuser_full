# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/26165150.py generated: Wed, 25 Jan 2017 15:25:24
#
# Event Type: 26165150
#
# ASCII decay Descriptor: [ Xi_cc+ -> ( Xi_c0 -> ( Xi- -> ( Lambda0 -> p+ pi- ) pi+ ) pi+ ) pi+ ]cc
#
from Configurables import Generation
Generation().EventType = 26165150
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "GenXiccProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import GenXiccProduction
Generation().Special.addTool( GenXiccProduction )
Generation().Special.GenXiccProduction.BaryonState = "Xi_cc+"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xicc_Xic0pi,Xipi=DecProdCut,WithMinPT.dec"
Generation().Special.CutTool = "XiccDaughtersInLHCbAndWithMinPT"
from Configurables import XiccDaughtersInLHCbAndWithMinPT
Generation().Special.addTool( XiccDaughtersInLHCbAndWithMinPT )
Generation().Special.XiccDaughtersInLHCbAndWithMinPT.BaryonState = Generation().Special.GenXiccProduction.BaryonState
