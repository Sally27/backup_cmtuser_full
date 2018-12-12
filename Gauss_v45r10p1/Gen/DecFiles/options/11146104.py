# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11146104.py generated: Wed, 25 Jan 2017 15:25:24
#
# Event Type: 11146104
#
# ASCII decay Descriptor: [B0 -> (eta_prime -> pi+ pi- gamma) (KS0 -> pi+ pi-) (J/psi(1S) -> mu+ mu-)]cc
#
from Configurables import Generation
Generation().EventType = 11146104
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_JpsiKsetap,mm,pi+pi-g=DecProdCut,PHSP.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
