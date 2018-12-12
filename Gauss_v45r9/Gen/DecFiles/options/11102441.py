# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11102441.py generated: Fri, 27 Mar 2015 16:10:14
#
# Event Type: 11102441
#
# ASCII decay Descriptor: {[[B0]nos -> (K*(892)0 -> K+ pi-) (eta -> gamma gamma)]cc, [[B0]os -> (K*(892)~0 -> K- pi+) (eta -> gamma gamma)]cc}
#
from Configurables import Generation
Generation().EventType = 11102441
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Ksteta,gg=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
