# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/26266022.py generated: Wed, 25 Jan 2017 15:25:29
#
# Event Type: 26266022
#
# ASCII decay Descriptor: [ Sigma_c++ -> (Lambda_c+ -> p+ K- pi+) K- pi+ pi+ ]CC
#
from Configurables import Generation
Generation().EventType = 26266022
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xicc++_LcKpipi,pKpi=PPchange,DecProdCut,WithMinPT.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/DaughtersInLHCbAndWithMinPT"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 4222,-4222 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ " Sigma_c++              85        4222   2.0      3.50000000      3.330000e-13                 Sigma_c++        4222      0.00000000", " Sigma_c~--             86       -4222  -2.0      3.50000000      3.330000e-13            anti-Sigma_c--       -4222      0.00000000" ]

#
from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
gen = Generation()
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'DaughtersInLHCbAndWithMinPT' )
daughtersInLHCbAndWithMinPT = gen.SignalRepeatedHadronization.DaughtersInLHCbAndWithMinPT
daughtersInLHCbAndWithMinPT.Decay     = '^[ Sigma_c++ -> ^(Lambda_c+ --> ^p+ ^K- ^pi+) ^K- ^pi+ ^pi+ ]CC'
daughtersInLHCbAndWithMinPT.Preambulo += [
    'from GaudiKernel.SystemOfUnits import MeV ',
    'inAcc     = in_range ( 0.010 , GTHETA , 0.400 ) ',
    'protP     = ( GP > 8000 * MeV )',
    'xiccpT    = ( GPT > 2000 * MeV )'
]
daughtersInLHCbAndWithMinPT.Cuts      =    {
    '[pi+]cc'         : 'inAcc',
    '[K+]cc'          : 'inAcc',
    '[p+]cc'          : 'inAcc & protP',
    '[Sigma_c++]cc'   : 'xiccpT',
    }

Generation().SignalRepeatedHadronization.SignalPIDList = [ 4222, -4222 ]
