# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/14295001.py generated: Fri, 27 Mar 2015 16:10:00
#
# Event Type: 14295001
#
# ASCII decay Descriptor: [B_c+ -> (D+ => K- pi+ pi+) (D~0 -> K+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 14295001
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_D0D-DDalitz=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
