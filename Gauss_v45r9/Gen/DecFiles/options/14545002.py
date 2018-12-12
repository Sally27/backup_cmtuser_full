# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/14545002.py generated: Fri, 27 Mar 2015 16:10:12
#
# Event Type: 14545002
#
# ASCII decay Descriptor: [B_c+ -> (JPsi -> mu+ mu-) (K*+ -> (K_S0 -> pi+ pi-) pi+ )]cc
#
from Configurables import Generation
Generation().EventType = 14545002
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_JpsiKst=DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
