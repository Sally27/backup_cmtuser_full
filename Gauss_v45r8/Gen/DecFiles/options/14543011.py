# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/14543011.py generated: Fri, 27 Mar 2015 15:48:01
#
# Event Type: 14543011
#
# ASCII decay Descriptor: [B_c+ -> (JPsi -> mu+ mu-) (tau+ -> mu+ nu_mu anti-nu_tau) nu_tau]cc
#
from Configurables import Generation
Generation().EventType = 14543011
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_JpsiTauNu,mununu=DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
