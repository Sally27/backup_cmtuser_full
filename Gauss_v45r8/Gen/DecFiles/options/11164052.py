# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11164052.py generated: Fri, 27 Mar 2015 15:48:09
#
# Event Type: 11164052
#
# ASCII decay Descriptor: {[[B0]nos -> (D_s- => K+ K- pi-) pi+]cc, [[B0]os -> (D_s+ => K- K+ pi+) pi-]cc}
#
from Configurables import Generation
Generation().EventType = 11164052
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Ds-pi+,KKpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
