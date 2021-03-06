# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/43114001.py generated: Wed, 25 Jan 2017 15:25:36
#
# Event Type: 43114001
#
# ASCII decay Descriptor: pp->(  H_20 -> ( H_30 -> mu+ mu- ) ( H_30 -> mu+ mu-) )
#
from Configurables import Generation
Generation().EventType = 43114001
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Higgs_AA_mumumumu,mH=125GeV,mA=7GeV,tA=100ps,HidValley.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/TwoMuonsFromHVPionInAcceptance"
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "H_20 88 35 0.0 125.0 1.65e-22 Higgs'0 35 4.0e-03" , "H_30 89 36 0.0   7.0 1.0e-10      A0 36 0.0e+00" ]

from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/HidValleyH.py" )

Generation().Special.PythiaProduction.Commands[:0] = [
    "pyinit pdtinput $DECFILESROOT/ppfiles/HiddenValleyHiggses_mumu.pdt"
]

from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "TwoMuonsFromHVPionInAcceptance" )
tracksInAcc = Generation().TwoMuonsFromHVPionInAcceptance
tracksInAcc.Code = " count ( isGoodDVfromHVPion ) > 0 "
tracksInAcc.Preambulo += [
      "from GaudiKernel.SystemOfUnits import ns, GeV, mrad"
    , "isHVPion           = ( 'H_30' == GID )"
    , "isGoodDVDaughterMu = ( (~GVEV) & ( GP > 2.0*GeV ) & ( GTHETA < 400.0*mrad ) & ( 'mu+' == GABSID ) )"
    , "isGoodDVfromHVPion = ( isHVPion & ( GNINTREE( isGoodDVDaughterMu, 4 ) > 1 ) )"
    ]

