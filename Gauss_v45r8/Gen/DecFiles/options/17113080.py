# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/17113080.py generated: Fri, 27 Mar 2015 15:48:09
#
# Event Type: 17113080
#
# ASCII decay Descriptor: {[B*_s20 -> (B+ -> K+ mu+ tau-) K-]cc, [B*_s20 -> (B+ -> K+ mu- tau+) K-]cc}
#
from Configurables import Generation
Generation().EventType = 17113080
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bs2st_BuK,Kmutau=KKmuInAcc.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/KKMuonInAcc"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 535,-535 ]


from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
Generation().SignalRepeatedHadronization.addTool( LoKi__GenCutTool,'KKMuonInAcc')
kkmuInAcc = Generation().SignalRepeatedHadronization.KKMuonInAcc
kkmuInAcc.Decay = '[ (B*_s20 => (B+ => ^K+ ^mu+ tau-) ^K-) || (B*_s20 => (B+ => ^K+ ^mu- tau+) ^K-) ]CC'
kkmuInAcc.Preambulo += [
    'inAcc        = (in_range(0.005, GTHETA, 0.400))'
    ]
kkmuInAcc.Cuts = {
    '[mu+]cc'  : 'inAcc',
    '[K+]cc'   : 'inAcc'
    }


