# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11166762.py generated: Wed, 25 Jan 2017 15:25:27
#
# Event Type: 11166762
#
# ASCII decay Descriptor: {[[B0]nos => (K_S0 -> pi+ pi-) (D*(2010)- -> {(D- => K+ pi- pi-)pi0, (D- => K+ pi- pi-)gamma}) K+]cc, [[B0]os => (K_S0 -> pi+ pi-) (D*(2010)+ -> {(D+ => K- pi+ pi+)pi0, (D+ => K+ pi- pi-)gamma}) K-]cc}
#
from Configurables import Generation
Generation().EventType = 11166762
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dst-KSK,Kpipi=sqDalitz,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
