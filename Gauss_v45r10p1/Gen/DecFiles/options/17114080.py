# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/17114080.py generated: Wed, 25 Jan 2017 15:25:17
#
# Event Type: 17114080
#
# ASCII decay Descriptor: [B*_s20 -> (B+ -> K+ mu+ mu-) K-]cc
#
from Configurables import Generation
Generation().EventType = 17114080
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bs2st_BuK,Kmumu=KKmuInAcc.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 535,-535 ]


from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
Generation().SignalRepeatedHadronization.addTool( LoKi__GenCutTool,'TightCut')
kkmuInAcc = Generation().SignalRepeatedHadronization.TightCut
kkmuInAcc.Decay = '[B*_s20 => ^(B+ => ^K+ ^mu+ ^mu-) ^K-]CC'
kkmuInAcc.Preambulo += [
    'inAcc        = (in_range(0.01, GTHETA, 0.400))',
    'oneMuonInAcc = (GNINTREE( ("mu-"==GABSID) & inAcc) >= 1)'
    ]
kkmuInAcc.Cuts = {
    '[B+]cc'   : 'oneMuonInAcc',
    '[K+]cc'   : 'inAcc'
    }


