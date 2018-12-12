# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11266002.py generated: Fri, 27 Mar 2015 16:10:12
#
# Event Type: 11266002
#
# ASCII decay Descriptor: {[[B0]nos -> (D- => K+ pi- pi-) pi+ pi- pi+]cc, [[B0]os -> (D+ => K- pi+ pi+) pi- pi+ pi-]cc}
#
from Configurables import Generation
Generation().EventType = 11266002
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D-PiPiPi+=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
