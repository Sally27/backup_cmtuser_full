# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/14845017.py generated: Wed, 25 Jan 2017 15:25:26
#
# Event Type: 14845017
#
# ASCII decay Descriptor: [B_c+ => (psi(2S) --> (J/psi(1S) -> mu+ mu-) ...) (tau+ => mu+ nu_mu nu_tau~) nu_tau]CC
#
from Configurables import Generation
Generation().EventType = 14845017
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_psi2STauNu,Jpsi,mununu=BcVegPy,ffKiselev,JpsiLeptonInAcceptance.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
from Configurables import BcDaughtersInLHCb
Generation().Special.addTool( BcDaughtersInLHCb )
Generation().Special.BcDaughtersInLHCb.ChargedThetaMin = 0.
Generation().Special.BcDaughtersInLHCb.ChargedThetaMax = 10.
Generation().Special.BcDaughtersInLHCb.NeutralThetaMin = 0.
Generation().Special.BcDaughtersInLHCb.NeutralThetaMax = 10.
Generation().FullGenEventCutTool = "JpsiLeptonInAcceptance"

from Configurables import JpsiLeptonInAcceptance
Generation().addTool( JpsiLeptonInAcceptance )
Generation().JpsiLeptonInAcceptance.JpsiLepPMin = 0
Generation().JpsiLeptonInAcceptance.BachLepPMin = 0
Generation().JpsiLeptonInAcceptance.PreselMass = False
Generation().JpsiLeptonInAcceptance.PreselDoca = False

