# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11396410.py generated: Wed, 25 Jan 2017 15:25:22
#
# Event Type: 11396410
#
# ASCII decay Descriptor: [B0-> (D*- -> ((D- -> K+ pi- pi-) || (D- -> K+ K- pi-)) (pi0 , gammma)) (D*+ -> (D0 -> K- pi+) pi+)]cc
#
from Configurables import Generation
Generation().EventType = 11396410
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dst-Dst+,D-pi0,D0pi+=DDALITZ,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
