# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/43900053.py generated: Fri, 27 Mar 2015 16:10:13
#
# Event Type: 43900053
#
# ASCII decay Descriptor: pp->(  H_20 -> ( H_30 -> b anti-b ) ( H_30 -> b anti-b) )
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/HidValleyH.py" )
from Configurables import Generation
Generation().EventType = 43900053
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Higgs_AA_bbbb,mH=125GeV,mA=20GeV,tA=0ps.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/FourbFromH0InAcceptance"
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "H_20 88 35 0.0 125.0 9.4e-26 Higgs'0 35 0.0e+00" , "H_30 89 36 0.0  20.0 9.4e-26      A0 36 0.0e+00" ]

from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "FourbFromH0InAcceptance" )
tracksInAcc = Generation().FourbFromH0InAcceptance
tracksInAcc.Code = " count ( H0has4bin ) > 0 "
## - HepMC::IteratorRange::descendants   4
tracksInAcc.Preambulo += [
      "from GaudiKernel.SystemOfUnits import ns, GeV, mrad"
    , "isH0              = ( 'H_20' == GID)"
    , "isbin             = ( ('b' == GABSID) & (GTHETA < 400.0*mrad))"
    , "H0has4bin = (isH0 & ( GNINTREE(isbin , 4 ) > 3 ) )"
     ]

