# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11134002.py generated: Wed, 25 Jan 2017 15:25:21
#
# Event Type: 11134002
#
# ASCII decay Descriptor: {[ B0 -> K+ pi- (eta_c(1S) -> p+ p~-) ]CC}
#
from Configurables import Generation
Generation().EventType = 11134002
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_etacKpi=sqDalitz,pp=DecProdCut,TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]

# 
from Configurables import LoKi__GenCutTool 
gen = Generation() 
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' ) 
# 
tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay     = '^[ B0 -> ^K+ ^pi- ( eta_c(1S) => ^p+ ^p~- ) ]CC'
tightCut.Cuts      =    {
    '[B0]cc'   : ' goodB  ' , 
    '[p+]cc'   : ' goodProton  ' , 
    '[K+]cc'    : ' goodKaon  ' , 
    'eta_c(1S)' : ' goodEtac ',
    '[pi+]cc'   : ' goodPion  ' }
tightCut.Preambulo += [
    'from GaudiKernel.SystemOfUnits import ns',
    'from GaudiKernel.PhysicalConstants import c_light',
    'inAcc = in_range( 0.005, GTHETA, 0.400)',
    'goodProton  = ( GPT > 250  * MeV ) & inAcc' , 
    'goodKaon  = ( GPT > 150  * MeV )  & inAcc' , 
    'goodPion  = ( GPT > 150  * MeV ) & inAcc' ,
    'goodEtac  = in_range( 1.8, GY, 4.5)' ,
    'goodB  = ( GCTAU > 0.1e-3 * ns * c_light)' ]


