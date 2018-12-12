# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/14543007.py generated: Fri, 27 Mar 2015 15:48:14
#
# Event Type: 14543007
#
# ASCII decay Descriptor: [B_c+ => (J/psi(1S) => mu+ mu-) mu+ nu_mu]CC
#
from Configurables import Generation
Generation().EventType = 14543007
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_JpsiMuNu,mm=BcVegPy,ffKiselev.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
