# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11144021.py generated: Fri, 27 Mar 2015 15:48:13
#
# Event Type: 11144021
#
# ASCII decay Descriptor: {[[B0]nos -> ( psi(2S) -> mu+ mu-) (rho0 -> pi+ pi-)]cc, [[B0]os -> (J/psi(1S) -> mu+ mu-) (rho0 -> pi- pi+)]cc}
#
from Configurables import Generation
Generation().EventType = 11144021
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_psi2Srho0,mmpipi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
