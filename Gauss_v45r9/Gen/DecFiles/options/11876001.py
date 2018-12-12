# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11876001.py generated: Fri, 27 Mar 2015 16:10:07
#
# Event Type: 11876001
#
# ASCII decay Descriptor: [B0-> (Ds+ -> (phi -> K- K+) pi+) (D*- -> (anti-D0 -> K+ mu- anti-nu_mu ) pi- ) )]cc
#
from Configurables import Generation
Generation().EventType = 11876001
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_DsDst,phipiDpi,KKmunuX=cocktail,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LHCbAcceptance"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
