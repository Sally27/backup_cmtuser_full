# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11174204.py generated: Fri, 27 Mar 2015 16:10:11
#
# Event Type: 11174204
#
# ASCII decay Descriptor: {[[B0]nos -> (chi_c1(1P) -> gamma (J/psi(1S) -> mu+ mu- )) K+ pi-]cc, [[B0]os -> (chi_c1(1P) -> gamma (J/psi(1S) -> mu+ mu-)) K- pi+]cc}
#
from Configurables import Generation
Generation().EventType = 11174204
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_chic1Kpi,Jpsig,mm=Tight.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]

#
from Configurables import LoKi__GenCutTool 
gen = Generation() 
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' ) 
# 
tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay = '^[ Beauty =>  ( ( chi_c1(1P) => ^gamma ^(J/psi(1S) => ^mu+ ^mu- ) ) ) ^K+ ^pi- ]CC'
tightCut.Cuts      =    {
    'gamma'     : ' goodGamma ' ,
    '[mu+]cc'   : ' goodMuon  ' , 
    '[K+]cc'    : ' goodKaon  ' , 
    '[pi+]cc'   : ' goodPion  ' , 
    'J/psi(1S)' : ' goodPsi   ' ,
    '[B0]cc'    : ' goodB     ', }
tightCut.Preambulo += [  "GY = LoKi.GenParticles.Rapidity()" ]
tightCut.Preambulo += [
    'from GaudiKernel.SystemOfUnits import ns',
    'from GaudiKernel.PhysicalConstants import c_light',
    'inAcc     = in_range ( 0.005 , GTHETA , 0.400 ) ' , 
    'inEcalX   = abs ( GPX / GPZ ) < 4.5 / 12.5      ' , 
    'inEcalY   = abs ( GPY / GPZ ) < 3.5 / 12.5      ' , 
    'goodMuon  = ( GPT > 500  * MeV ) & ( GP > 6 * GeV )     & inAcc   ' , 
    'goodKaon  = ( GPT > 150  * MeV )                        & inAcc   ' , 
    'goodPion  = ( GPT > 150  * MeV )                        & inAcc   ' , 
    'goodGamma = ( 0 < GPZ ) & ( 150 * MeV < GPT ) & inEcalX & inEcalY ' ,
    'goodPsi   = ( GPT > 1000  * MeV ) & in_range( 1.8 , GY , 4.5 )'    ,
    'goodB     = ( GCTAU > 0.1e-3 * ns * c_light ) ', ]


