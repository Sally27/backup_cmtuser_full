# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/14375212.py generated: Fri, 27 Mar 2015 16:10:00
#
# Event Type: 14375212
#
# ASCII decay Descriptor: [B_c+ -> (J/psi(1S) -> mu+ mu-) (D_s*+ -> (D_s+ -> pi+ pi- pi+) gamma/pi0) ]cc
#
from Configurables import Generation
Generation().EventType = 14375212
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_JpsiDsStar+,mmpipipi=DDalitz,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
