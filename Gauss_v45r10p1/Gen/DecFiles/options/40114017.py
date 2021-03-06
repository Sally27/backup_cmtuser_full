# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/40114017.py generated: Wed, 25 Jan 2017 15:25:30
#
# Event Type: 40114017
#
# ASCII decay Descriptor: Higgs'0 -> ( A0 -> mu+ mu- ) ( A0 -> mu+ mu-)
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/HiggsNarrow,2GeV_2A14mu.py" )
from Configurables import Generation
Generation().EventType = 40114017
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Higgs_AA_mumumumu,mH=2GeV,mA=0.25GeV,tA=90ps,Hnarrow.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/TwoMuonsFromA1InAcceptance"
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "H_20 88 35 0.0 2.0 1.03e-20 Higgs'0 35 0.0e+00" , "H_30 89 36 0.0   0.25 8.95e-11      A0 36 0.0e+00" ]
                                                                                           
from Gaudi.Configuration import *  
from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "TwoMuonsFromA1InAcceptance" )
tracksInAcc = Generation().TwoMuonsFromA1InAcceptance
tracksInAcc.Code = " count ( isGoodDVfromA1 ) > 1 "
### - HepMC::IteratorRange::descendants   4
tracksInAcc.Preambulo += [
      "from GaudiKernel.SystemOfUnits import GeV, mrad"
    , "isA1           = ( 'H_30' == GID )"
    , "isGoodDVDaughterMu = ( ( ~GVEV ) & ( GTHETA < 400.0*mrad ) & ( 'mu+' == GABSID ) )"
    , "isGoodDVfromA1 = ( isA1 & ( GNINTREE( isGoodDVDaughterMu, 4 ) > 1 ) )"
    ]

