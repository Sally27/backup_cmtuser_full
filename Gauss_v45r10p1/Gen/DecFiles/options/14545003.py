# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/14545003.py generated: Wed, 25 Jan 2017 15:25:22
#
# Event Type: 14545003
#
# ASCII decay Descriptor: [B_c+ -> (JPsi -> mu+ mu-) (tau+ -> pi+ pi+ pi- anti-nu_tau) nu_tau]cc
#
from Configurables import Generation
Generation().EventType = 14545003
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_JpsiTauNu=TightDecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/TightCuts"

from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "TightCuts" )
tightCuts = Generation().TightCuts
tightCuts.Code = "( count ( hasGoodTau ) > 0 ) & ( count ( hasGoodJpsi ) > 0 )"

tightCuts.Preambulo += [
      "from GaudiKernel.SystemOfUnits import ns, GeV, mrad"
    , "hasGoodTau        = (( 'tau+'      == GABSID ) & ( GNINTREE( ( 'pi+' == GABSID ) & ( in_range(0.075,GTHETA,0.400) ) & ( GPT > 0.15*GeV ) & ( GP > 2*GeV )) == 3 ))"
    , "hasGoodJpsi       = (( 'J/psi(1S)' == GABSID ) & ( GNINTREE( ( 'mu+' == GABSID ) & ( in_range(0.075,GTHETA,0.400) ) & ( GPT > 0.50*GeV ) & ( GP > 2*GeV )) == 2 ))"
     ]

