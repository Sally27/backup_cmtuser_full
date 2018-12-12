# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11714001.py generated: Wed, 25 Jan 2017 15:25:31
#
# Event Type: 11714001
#
# ASCII decay Descriptor: {[[B0]nos -> mu+ (tau- -> mu- anti-nu_mu nu_tau) (K*(892)0 -> K+ pi-)]cc, [[B0]nos -> (tau+ -> mu+ nu_mu anti-nu_tau) mu- (K*(892)0 -> K+ pi-)]cc, [[B0]os -> mu- (tau+ -> mu+ nu_mu anti-nu_tau) (K*(892)~0 -> K- pi+)]cc, [[B0]os -> (tau- -> mu- anti-nu_mu nu_tau) mu+ (K*(892)~0 -> K- pi+)]cc}
#
from Configurables import Generation
Generation().EventType = 11714001
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Ksttaumu,mu=DecProdCut,phsp.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
