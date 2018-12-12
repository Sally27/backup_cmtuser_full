# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/14643048.py generated: Fri, 27 Mar 2015 16:10:04
#
# Event Type: 14643048
#
# ASCII decay Descriptor: [B_c+ => (J/psi(1S) => mu+ mu-) (tau+ => mu+ nu_mu nu_tau~) nu_tau]CC
#
from Configurables import Generation
Generation().EventType = 14643048
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_JpsiTauNu,mununu=BcVegPy,ffEbert.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
