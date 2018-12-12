# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11134020.py generated: Wed, 25 Jan 2017 15:25:27
#
# Event Type: 11134020
#
# ASCII decay Descriptor: {[[B0]nos -> (J/psi(1S) -> p+ p~-) (rho(770)0 -> pi+ pi-)]cc, [[B0]os -> (J/psi(1S) -> p+ p~-) (rho(770)0 -> pi- pi+)]cc}
#
from Configurables import Generation
Generation().EventType = 11134020
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Jpsirho0,pp=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
