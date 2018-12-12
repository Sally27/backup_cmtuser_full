# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11112411.py generated: Fri, 27 Mar 2015 16:10:04
#
# Event Type: 11112411
#
# ASCII decay Descriptor: [B0 -> (K_S0 -> pi0 pi0) mu+ mu-]cc
#
from Configurables import Generation
Generation().EventType = 11112411
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_KSmumu,pi0pi0=OnePi0ReqInAcc.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/OnePi0ReqInAcc"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]


from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
Generation().SignalRepeatedHadronization.addTool( LoKi__GenCutTool,'OnePi0ReqInAcc')
pi0mmInAcc = Generation().SignalRepeatedHadronization.OnePi0ReqInAcc
pi0mmInAcc.Decay = '[B0 -> ^(KS0 -> ^pi0 ^pi0) ^mu+ ^mu-]CC'
pi0mmInAcc.Preambulo += [
   'inAcc        = (in_range(0.005, GTHETA, 0.400))',
   'KSDaugPiInAcc = (GNINTREE( ("pi0"==GABSID) & inAcc) >= 1)',
]
pi0mmInAcc.Cuts = {
   '[KS0]cc'  : 'KSDaugPiInAcc',
   'mu+'      : 'inAcc',
   'mu-'      : 'inAcc'
   }

