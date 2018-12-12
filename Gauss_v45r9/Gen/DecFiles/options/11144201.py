# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11144201.py generated: Fri, 27 Mar 2015 16:10:00
#
# Event Type: 11144201
#
# ASCII decay Descriptor: {[[B0]nos -> (chi_c1(1P) -> gamma (J/psi(1S) -> mu+ mu- )) K+ pi-]cc, [[B0]os -> (chi_c1(1P) -> gamma (J/psi(1S) -> mu+ mu-)) K- pi+]cc}
#
from Configurables import Generation
Generation().EventType = 11144201
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_chic1Kpi,mm=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
