# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/14547001.py generated: Fri, 27 Mar 2015 15:47:57
#
# Event Type: 14547001
#
# ASCII decay Descriptor: [B_c+ -> (psi (Jpsi -> mu+ mu-) X) (tau+ -> pi+ pi+ pi- anti-nu_tau) nu_tau]cc
#
from Configurables import Generation
Generation().EventType = 14547001
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_psi2STauNu,Jpsi,mm=DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
from Configurables import BcDaughtersInLHCb
Generation().Special.addTool( BcDaughtersInLHCb )
Generation().Special.BcDaughtersInLHCb.NeutralThetaMin = 0.0
Generation().Special.BcDaughtersInLHCb.NeutralThetaMax = 3.14
Generation().Special.BcDaughtersInLHCb.ChargedThetaMax = 0.5
