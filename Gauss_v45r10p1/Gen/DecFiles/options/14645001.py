# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/14645001.py generated: Wed, 25 Jan 2017 15:25:24
#
# Event Type: 14645001
#
# ASCII decay Descriptor: [B_c+ -> (JPsi -> mu+ mu-) (D_s+ -> (tau+ -> pi+ pi+ pi- anti-nu_tau) nu_tau)]cc
#
from Configurables import Generation
Generation().EventType = 14645001
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_JpsiInclc,TauNu=DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
