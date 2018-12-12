# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/14375213.py generated: Wed, 25 Jan 2017 15:25:20
#
# Event Type: 14375213
#
# ASCII decay Descriptor: [B_c+ -> (J/psi(1S) -> mu+ mu-) (D_s*+ -> (D_s+ -> pi+ pi- pi+) gamma/pi0) ]cc
#
from Configurables import Generation
Generation().EventType = 14375213
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_JpsiDsStar+,mmpipipi=DDalitz,DecProdCut,Apm.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
