# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/14745001.py generated: Fri, 27 Mar 2015 15:47:57
#
# Event Type: 14745001
#
# ASCII decay Descriptor: [B_c+ -> (JPsi -> mu+ mu-) ({D+,D_s+,D*+,D_s*+} -> X)]cc
#
from Configurables import Generation
Generation().EventType = 14745001
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_JpsiInclc,3track,miss=DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
