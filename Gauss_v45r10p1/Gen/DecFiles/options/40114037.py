# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/40114037.py generated: Wed, 25 Jan 2017 15:25:21
#
# Event Type: 40114037
#
# ASCII decay Descriptor: Higgs'0 -> (A0 -> mu+ mu-) (A0 -> mu+ mu-)
#
from Configurables import Generation
Generation().EventType = 40114037
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "Pythia8Production"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Higgs_AA_mumumumu,mH=50GeV,mA=2.5GeV,tA=100ps,Hnarrow.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/TwoMuonsFromA1InAcceptance"
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "H_20 88 35 0.0 50.0 2.06e-21 Higgs'0 35 0.0e+00", "H_30 89 36 0.0 2.5 1e-10 A0 36 0.0e+00" ]

from Gaudi.Configuration import *
from Configurables import LoKi__FullGenEventCut
Generation().addTool(LoKi__FullGenEventCut, "TwoMuonsFromA1InAcceptance")
tracksInAcc = Generation().TwoMuonsFromA1InAcceptance
tracksInAcc.Code = "count(isGoodDVfromA1) > 1"
tracksInAcc.Preambulo += [
      "from GaudiKernel.SystemOfUnits import GeV, mrad",
      "isA1 = ('H_30' == GID)",
      "isGoodDVDaughterMu = ((~GVEV) & (GTHETA < 400.0*mrad) "
      "& ('mu+' == GABSID))",
      "isGoodDVfromA1 = (isA1 & (GNINTREE(isGoodDVDaughterMu, 4) > 1))"]
from Gaudi.Configuration import importOptions
importOptions("$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py")
from Configurables import Pythia8Production
Generation().Special.addTool(Pythia8Production)
Generation().Special.Pythia8Production.Commands += [
    "Higgs:useBSM = on", "HiggsBSM:allH2 = on", "35:mWidth = 1.60e-03",
    "35:m0 = 50.0", "35:doForceWidth = true", "35:doExternalDecay = true"]

