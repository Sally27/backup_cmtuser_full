# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11574030.py generated: Wed, 25 Jan 2017 15:25:34
#
# Event Type: 11574030
#
# ASCII decay Descriptor: {[[B0]nos -> (D- -> (K*(892)0 -> K+ pi-) mu- anti-nu_mu) mu+ nu_mu ]cc, [[B0]os -> (D+ -> (K*(892)~0 -> K- pi+) mu+ nu_mu) mu- anti-nu_mu ]cc}
#
from Configurables import Generation
Generation().EventType = 11574030
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dmunu,Kstmunu=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
