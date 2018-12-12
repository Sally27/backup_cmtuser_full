# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/14265001.py generated: Fri, 27 Mar 2015 16:10:01
#
# Event Type: 14265001
#
# ASCII decay Descriptor: [B_c+ -> (D_s+ => K- K+ pi+) (phi -> K+ K-)]cc
#
from Configurables import Generation
Generation().EventType = 14265001
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_Dsphi-DDalitz=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
