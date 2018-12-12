# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/14545010.py generated: Fri, 27 Mar 2015 16:10:09
#
# Event Type: 14545010
#
# ASCII decay Descriptor: [B_c+ -> (JPsi -> mu+ mu-) (tau+ -> K+ pi+ pi- anti-nu_tau) nu_tau]cc
#
from Configurables import Generation
Generation().EventType = 14545010
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_JpsiTauNu,Kpipinu=DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
