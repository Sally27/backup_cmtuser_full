# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/49011004.py generated: Wed, 25 Jan 2017 15:25:26
#
# Event Type: 49011004
#
# ASCII decay Descriptor: pp => bbbar (=> muX)
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/HardQCD_ccbar.py" )
from Configurables import Generation
Generation().EventType = 49011004
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "Pythia8Production"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/ccbar=HardQCD,pt18GeV,mu.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/HighPtMuonInAcc"

from Configurables import LoKi__FullGenEventCut
Generation().addTool(LoKi__FullGenEventCut, 'HighPtMuonInAcc')
cutTool = Generation().HighPtMuonInAcc
cutTool.Code = 'count(HighPtMuonInAcc) > 0'
cutTool.Preambulo += [
   'from GaudiKernel.SystemOfUnits import ns, GeV, mrad',
   'GPT = LoKi.GenParticles.TransverseMomentum()',
   'isMuon = (GABSID == 13)',
   'highPT = ((GTHETA < 400.0*mrad) & (GPT > 18*GeV))',
   'HighPtMuonInAcc = ((isMuon) & (highPT))'
   ]

