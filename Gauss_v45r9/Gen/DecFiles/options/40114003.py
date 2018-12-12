# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/40114003.py generated: Fri, 27 Mar 2015 16:10:16
#
# Event Type: 40114003
#
# ASCII decay Descriptor: Higgs'0 -> ( A0 -> mu+ mu- ) ( A0 -> mu+ mu-)
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/HiggsNarrow,10GeV_2A14mu.py" )
from Configurables import Generation
Generation().EventType = 40114003
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Higgs_AA_mumumumu,mH=10GeV,mA=0.75GeV,tA=0ps,Hnarrow,Anarrow.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/TwoMuonsFromA1InAcceptance"
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "H_20 88 35 0.0 10.0 2.06e-21 Higgs'0 35 0.0e+00" , "H_30 89 36 0.0   0.75 2.74e-20      A0 36 0.0e+00" ]
                                                                                           
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

