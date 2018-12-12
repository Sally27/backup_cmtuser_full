# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/14145042.py generated: Fri, 27 Mar 2015 16:10:11
#
# Event Type: 14145042
#
# ASCII decay Descriptor: [B_c+ -> (J/psi(1S) -> mu+ mu- ) pi+ pi+ pi-]cc
#
from Configurables import Generation
Generation().EventType = 14145042
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_Jpsipipipi,mm=BcVegPy,BCVHAD2.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
