# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/42912011.py generated: Wed, 25 Jan 2017 15:25:31
#
# Event Type: 42912011
#
# ASCII decay Descriptor: pp -> ( WR- -> ( mu- (nu_Rmu -> mu- jet ) ) )
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/WRmuHeavyN.py" )
from Configurables import Generation
Generation().EventType = 42912011
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/W_mumuqq,mN=5GeV,tN=10ps.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/HeavyNFromRWInAcceptance"
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "nu_Rmu     88     9900014    0       5.0    1.00000e-11   unknown  9900014   6.00000" , "W_R-       88     9900024    1    80.38500  0.00000e+00   unknown  9900024   0.00000" ]

Generation().Special.Pythia8Production.Commands += [
             "9900024:oneChannel = 1 1 0 -13 9900014"
      ]
from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "HeavyNFromRWInAcceptance" )
tracksInAcc = Generation().HeavyNFromRWInAcceptance
tracksInAcc.Code = " count ( isGoodVfromW ) > 0 "
tracksInAcc.Preambulo += [
"from GaudiKernel.SystemOfUnits import ns, GeV, mrad"
, "isHeavyN      = ( (GDECTREE('[ X -> mu+ ... ]CC')) & ( GTHETA < 400.0*mrad ) )"
, "isRW          = ( ('W_R-' == GABSID) )"
, "isGoodMuon    = ( ( GABSID == 13 ) & (~GVEV) & ( GP > 2.0*GeV ) & ( GTHETA < 400.0*mrad ) & ( GETA > 2) )"
, "isGoodVfromN  = ( isHeavyN & ( GNINTREE( isGoodMuon, HepMC.descendants ) >= 1 ) )"
, "isGoodVfromW  = ( isRW & ( GNINTREE( isGoodVfromN, HepMC.descendants ) == 1 ) & ( GNINTREE( isGoodMuon, HepMC.descendants ) >= 1 ) )"
]

